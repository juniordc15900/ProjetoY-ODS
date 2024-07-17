from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Usuario, Dominio, Sessao, Clique
import pyrebase
import firebase_admin
from firebase_admin import credentials, auth as firebase_auth
from django.conf import settings  
import os
from pathlib import Path

# Defina BASE_DIR
BASE_DIR = Path(__file__).resolve().parent.parent

config={
    "apiKey": "AIzaSyDfPjeLPW0cu5wFqfG6B_QnSc_1ODylIUA",
    "authDomain": "projeto-ods-ee6a9.firebaseapp.com",
    "projectId": "projeto-ods-ee6a9",
    "storageBucket": "projeto-ods-ee6a9.appspot.com",
    "messagingSenderId": "831716501782",
    "databaseURL" : "https://console.firebase.google.com/u/0/project/projeto-ods-ee6a9/database/projeto-ods-ee6a9-default-rtdb/data/~2F",
    "appId": "1:831716501782:web:0a338f2bd0d6c64e588837",
    "measurementId": "G-17Z1C4QTB3"
    }

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
database = firebase.database()
cred_path = os.path.join(settings.BASE_DIR, 'credenciais.json')  # Use settings.BASE_DIR
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)

@csrf_exempt
def registrar_usuario(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        preferencias = request.POST.get('preferencias', '{}')
        usuario = Usuario.objects.create(nome=nome, email=email, preferencias=preferencias)
        return JsonResponse({'status': 'success', 'usuario_id': usuario.id})
    return render(request, 'registrar_usuario.html')

@csrf_exempt
def adicionar_dominio(request):
    if request.method == 'POST':
        usuario_id = request.POST.get('usuario_id')
        nome = request.POST.get('nome')
        vencimento = request.POST.get('vencimento')
        valor = request.POST.get('valor')
        usuario = get_object_or_404(Usuario, id=usuario_id)
        dominio = Dominio.objects.create(usuario=usuario, nome=nome, vencimento=vencimento, valor=valor)
        return JsonResponse({'status': 'success', 'dominio_id': dominio.id})
    return render(request, 'adicionar_dominio.html')

@csrf_exempt
def iniciar_sessao(request):
    if request.method == 'POST':
        usuario_id = request.POST.get('usuario_id')
        usuario = get_object_or_404(Usuario, id=usuario_id)
        sessao = Sessao.objects.create(usuario=usuario)
        return JsonResponse({'status': 'success', 'sessao_id': sessao.id})
    return render(request, 'iniciar_sessao.html')

@csrf_exempt
def registrar_clique(request):
    if request.method == 'POST':
        sessao_id = request.POST.get('sessao_id')
        pagina = request.POST.get('pagina')
        elemento = request.POST.get('elemento')
        sessao = get_object_or_404(Sessao, id=sessao_id)
        clique = Clique.objects.create(sessao=sessao, pagina=pagina, elemento=elemento)
        return JsonResponse({'status': 'success', 'clique_id': clique.id})
    return render(request, 'registrar_clique.html')

def listar_dominios(request):
    if request.method == 'GET':
        usuario_id = request.GET.get('usuario_id')
        usuario = get_object_or_404(Usuario, id=usuario_id)
        dominios = usuario.dominios.all()
        dominios_data = [{'nome': dominio.nome, 'vencimento': dominio.vencimento, 'valor': dominio.valor} for dominio in dominios]
        return render(request, 'listar_dominios.html', {'dominios': dominios_data})
    return render(request, 'listar_dominios.html')

def login(request):
    return render(request, "login.html")

@csrf_exempt
def postsignIn(request):
    email = request.POST.get('email')
    pasw = request.POST.get('pass')
    try:
        user = auth.sign_in_with_email_and_password(email, pasw)
    except:
        message = "Invalid Credentials!! Please check your data"
        return render(request, "login.html", {"message": message})
    session_id = user['idToken']
    request.session['uid'] = str(session_id)
    return redirect('/home/')

def logout(request):
    try:
        del request.session['uid']
    except:
        pass
    return redirect('/login/')

@csrf_exempt
def google_login(request):
    if request.method == 'POST':
        token = request.POST.get('token')
        email = request.POST.get('email')
        try:
            decoded_token = firebase_auth.verify_id_token(token)
            uid = decoded_token['uid']
            user = Usuario.objects.filter(email=email).first()
            if not user:
                user = Usuario.objects.create(nome=decoded_token['name'], email=email)
            request.session['uid'] = uid
            return JsonResponse({'status': 'success'})
        except Exception as e:
            print(e)
            return JsonResponse({'status': 'error', 'message': 'Falha na autenticação com Google'})
    return JsonResponse({'status': 'error', 'message': 'Método não permitido'}, status=405)
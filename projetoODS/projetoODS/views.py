from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pyrebase

config={
    "apiKey": "AIzaSyDfPjeLPW0cu5wFqfG6B_QnSc_1ODylIUA",
    "authDomain": "projeto-ods-ee6a9.firebaseapp.com",
    "projectId": "projeto-ods-ee6a9",
    "storageBucket": "projeto-ods-ee6a9.appspot.com",
    "messagingSenderId": "831716501782",
    # "databaseURL" : "https://console.firebase.google.com/u/0/project/projeto-ods-ee6a9/database/projeto-ods-ee6a9-default-rtdb/data/~2F",
    "databaseURL": "https://projeto-ods-ee6a9-default-rtdb.firebaseio.com",
    "appId": "1:831716501782:web:0a338f2bd0d6c64e588837",
    "measurementId": "G-17Z1C4QTB3"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

@csrf_exempt
def signIn(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('pass')
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            return JsonResponse({"success": True, "message": "Login bem-sucedido"})
        except:
            return JsonResponse({"success": False, "message": "Credenciais inválidas! Por favor, verifique seus dados."})

@csrf_exempt
def signUp(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('pass')
        try:
            user = auth.create_user_with_email_and_password(email, password)
            return JsonResponse({"success": True, "message": "Cadastro bem-sucedido"})
        except:
            return JsonResponse({"success": False, "message": "Erro ao criar usuário. Tente novamente."})

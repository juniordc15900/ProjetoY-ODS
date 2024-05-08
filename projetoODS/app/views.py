from django.http import JsonResponse
from django.shortcuts import render
from django.middleware.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie
import pyrebase

config = {
    "apiKey": "AIzaSyDfPjeLPW0cu5wFqfG6B_QnSc_1ODylIUA",
    "authDomain": "projeto-ods-ee6a9.firebaseapp.com",
    "projectId": "projeto-ods-ee6a9",
    "storageBucket": "projeto-ods-ee6a9.appspot.com",
    "messagingSenderId": "831716501782",
    "databaseURL": "https://projeto-ods-ee6a9-default-rtdb.firebaseio.com",
    "appId": "1:831716501782:web:0a338f2bd0d6c64e588837",
    "measurementId": "G-17Z1C4QTB3"
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()


def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, "Home.html")


def signIn(request):
    return render(request, "Login.html")


@ensure_csrf_cookie  # Add this line
def postsignIn(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        pasw = request.POST.get('pass')
        try:
            user = authe.sign_in_with_email_and_password(email, pasw)
            session_id = user['idToken']
            request.session['uid'] = str(session_id)
            return JsonResponse({"email": email}, status=200)
        except Exception as e:
            print(e)
            message = "Invalid Credentials!! Please Check your Data"
            return JsonResponse({"message": message}, status=400)
    else:
        return JsonResponse({"error": "Method Not Allowed"}, status=405)


def logout(request):
    try:
        del request.session['uid']
    except:
        pass
    return render(request, "Login.html")


def signUp(request):
    return render(request, "Registration.html")


@ensure_csrf_cookie  # Add this line
def postsignUp(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        passs = request.POST.get('pass')
        name = request.POST.get('name')
        try:
            # Obter o token CSRF
            token = get_token(request)
            user = authe.create_user_with_email_and_password(email, passs)
            uid = user['localId']
            idtoken = request.session['uid']
            print(uid)
            return JsonResponse({"message": "User created successfully!"}, status=200)
        except Exception as e:
            print(e)
            return JsonResponse({"error": "Failed to create user"}, status=500)
    else:
        return JsonResponse({"error": "Method Not Allowed"}, status=405)


def get_csrf_token(request):
    token = get_token(request)
    return JsonResponse({'csrfToken': token})

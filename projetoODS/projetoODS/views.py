from django.shortcuts import render
from django.http import JsonResponse
import pyrebase

config = {
    "apiKey": "AIzaSyDfPjeLPW0cu5wFqfG6B_QnSc_1ODylIUA",
    "authDomain": "projeto-ods-ee6a9.firebaseapp.com",
    "projectId": "projeto-ods-ee6a9",
    "storageBucket": "projeto-ods-ee6a9.appspot.com",
    "messagingSenderId": "831716501782",
    "databaseURL": "https://console.firebase.google.com/u/0/project/projeto-ods-ee6a9/database/projeto-ods-ee6a9-default-rtdb/data/~2F",
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

def postsignIn(request):
    email = request.POST.get('email')
    pasw = request.POST.get('pass')
    try:
        # if there is no error then signin the user with given email and password
        user = authe.sign_in_with_email_and_password(email, pasw)
    except:
        message = "Invalid Credentials!!Please ChecK your Data"
        return render(request, "Login.html", {"message": message})
    session_id = user['idToken']
    request.session['uid'] = str(session_id)
    return render(request, "Home.html", {"email": email})

def logout(request):
    try:
        del request.session['uid']
    except:
        pass
    return render(request, "Login.html")

def signUp(request):
    return render(request, "Registration.html")

def postsignUp(request):
    email = request.POST.get('email')
    passs = request.POST.get('pass')
    name = request.POST.get('name')
    try:
        # creating a user with the given email and password
        user = authe.create_user_with_email_and_password(email, passs)
        uid = user['localId']
        idtoken = request.session['uid']
        print(uid)
    except:
        return render(request, "Registration.html")
    return render(request, "Login.html")

def reset_password(request):
    return render(request, "ResetPassword.html")

def post_reset_password(request):
    email = request.POST.get('email')
    try:
        authe.send_password_reset_email(email)
        message = "A reset link has been sent to your email address."
        return render(request, "Login.html", {"message": message})
    except:
        message = "An error occurred. Please check the email address."
        return render(request, "ResetPassword.html", {"message": message})
def google_sign_in(request):
    return render(request, "GoogleSignIn.html")

def post_google_sign_in(request):
    # This assumes you have a way to receive the Google ID token from the client
    id_token = request.POST.get('idToken')
    try:
        user = authe.sign_in_with_google(id_token)
        session_id = user['idToken']
        request.session['uid'] = str(session_id)
        return JsonResponse({"success": True, "email": user['email']})
    except:
        return JsonResponse({"success": False, "message": "Authentication failed."})

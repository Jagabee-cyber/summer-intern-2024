from django.shortcuts import render, HttpResponse

# Create your views here.
def show_login_page(request):
    return render(request, "login.html")

def createAccount(request):
    return render(request, "createAcc.html")

def addProject(request):
    return render(request, "addProject.html")

def mainSelection(request):
    return render(request, "mainSelection.html")

def landingPage(request):
    return render(request, "landingPage.html")

def testLogin(request):
    return render(request, "testlogin.html")

def galleryPage(request):
    return render(request, "galleryPage.html")

def viewProject(request):
    return render(request, "projectPage.html")




# from django.shortcuts import redirect
# from django.contrib.auth import logout
# from django.conf import settings
# def google_oauth_redirect(request):
#     # Replace with your actual Google client ID and redirect URI
#     client_id = "462879239975-uegrn3kasa9f4t929p2a1p3svrjr2i9a.apps.googleusercontent.com"
#     redirect_uri = request.build_absolute_uri('/accounts/google/login/callback/')
    
#     # Construct the OAuth URL
#     oauth_url = (
#         "https://accounts.google.com/o/oauth2/auth"
#         "?response_type=code"
#         f"&client_id={client_id}"
#         f"&redirect_uri={redirect_uri}"
#         "&scope=openid%20email%20profile"
#         "&access_type=online"
#         "&approval_prompt=auto"
#     )
    
#     return redirect(oauth_url)

'''
from django.http import JsonResponse
from django.contrib.auth import login
from django.contrib.auth.models import User
from firebase_admin import auth as firebase_auth

def firebase_login(request):
    if request.method == 'POST':
        token = request.POST.get('token')

        try:
            # Verify the token using Firebase Admin
            decoded_token = firebase_auth.verify_id_token(token)
            uid = decoded_token['uid']

            # Get or create the user based on Firebase UID
            user, created = User.objects.get_or_create(username=uid)

            # Log in the user
            login(request, user)  # Pass the user object to the login function

            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

'''
import firebase_admin
from firebase_admin import auth as firebase_auth
from django.http import JsonResponse

def login_view(request):
    token = request.POST.get('idToken')
    try:
        decoded_token = firebase_auth.verify_id_token(token)
        uid = decoded_token['uid']
        # You can now use the uid to authenticate the user in your Django app
        return JsonResponse({'status': 'success', 'uid': uid})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})
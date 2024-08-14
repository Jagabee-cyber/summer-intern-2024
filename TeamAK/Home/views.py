from django.shortcuts import render, HttpResponse

# Create your views here.
def login(request):
    return render(request, "login.html")

def createAccount(request):
    return render(request, "createAcc.html")

def addProject(request):
    return render(request, "addProject.html")
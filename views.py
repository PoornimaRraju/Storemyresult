from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def SRM(request):
    return render(request,'frontpage.html')
def home(request):
    return render(request,'home.html')
def signup(request):
    if request.method =='POST':
        firstname=request.POST['firstName']
        lastName=request.POST['lastName']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        if password==password2:
            user=User.objects.create_user(username=username,email=email,password=password,first_name=firstname,last_name=lastName)
            print("user created")
            return redirect('/accounts/login')
        else:
            print("wrong password")
    else:
        return render(request,'signup.html')
def login(request):
     if request.method =='POST':
        uname = request.POST['username']   
        password = request.POST['password'] 
        user = auth.authenticate(username=uname,password=password)
        if user is not None:
            auth.login(request,user)
            print("logged in")
            return redirect('/')
     else:
        return render(request,'login.html')
def contact(request):
    return render(request,'contact.html')
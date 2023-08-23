from django.shortcuts import render,redirect
from rest_framework.viewsets import ModelViewSet
from .models import blog
from .serializers import BlogSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import View
from .mypermission import CustomPermission
from rest_framework.views import APIView
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth

class signup(View):
    def get(self,request):
        return render(request,'signup.html')

    def post(self,request):
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,"email exists please go to login page")
                redirect('/signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,"username exists please enter different username")
                redirect('/signup')
            else:
                usr=User.objects.create_user(username=username,email=email,password=password1)
                usr.save()
                return redirect('/login') 
        else:
            messages.info(request,"password not matched")
            redirect('/signup')
        return render(request,'signup.html')



class login(View):
    def get(self,request):
        return render(request,'login.html')
    
    def post(self,request):
        username=request.POST['username']
        pwd=request.POST['password']
        usr=auth.authenticate(username=username,password=pwd)

        if usr is not None:
            auth.login(request,usr)
            return redirect('/home')
        else:
            messages.info(request,"enter valid credentials")
            return redirect('/login')
        

class logout(View):
    def get(self,request):
        auth.logout(request)
        redirect('/login')
        return render(request,'login.html')

def home(request):
    return render(request,'userdash.html')

def getblog(request):
    return render(request,'anondash.html')


class blogcls(ModelViewSet):
    queryset=blog.objects.all()
    serializer_class=BlogSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return blog.objects.filter(user=self.request.user)
        else:
            return blog.objects.all()

    def create(self, request):
        ser=BlogSerializer(context = {"request": request},data=request.data)
        if ser.is_valid():
            ser.save()
        return redirect('/home')
    

class dltobj(View):
    def get(self,request,pk):
        blg=blog.objects.get(id=pk)
        blg.delete()
        return redirect('/home')
    
class updateobj(APIView):
    permission_classes=[IsAuthenticatedOrReadOnly]
    def post(self,request,pk):
        blg=blog.objects.get(id=pk)
        serializer=BlogSerializer(blg,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
        return redirect('/home')
    
class bloganon(ModelViewSet):
    queryset=blog.objects.all()
    serializer_class=BlogSerializer
    permission_classes=[CustomPermission]
    
from django.shortcuts import render, redirect
from django.template import loader
from . models import spent, User
import datetime
from django.db.models import Sum
from .forms import Add_form
from django.contrib.auth.models import auth, User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.conf import settings
from rest_framework import viewsets, permissions
from . serializers import Spent_serializer, User_serializer
# Create your views here.


from django.http import HttpResponse
from . models import spent


def index(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            a=spent()
            a.user_name_id=request.user.id
            a.spent_on=request.POST.get('spent_on')
            a.reason=request.POST.get('reason')
            a.amount=request.POST.get('amount')
            a.time=datetime.datetime.now()
            a.save()
       
            
            return redirect('/')
        
        else:
            latest_question_list = spent.objects.filter(user_name=request.user.id)
            amount_sum=spent.objects.all().filter(user_name=request.user.id).aggregate(Sum('amount')).get('amount__sum', 0.00)
            template = loader.get_template('expense/index.html')
            context = {
                'latest_question_list': latest_question_list,
                'amount_sum': amount_sum,
            }
        
            return HttpResponse(template.render(context, request))
    else:
        return redirect('/login')

    
    
def new_index(request, question_id):
    new=spent.objects.filter(id=question_id).delete()
    print(new)
    return redirect("/")

def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']

        user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
        user.save()
        """  subject="hey " + first_name + " this is email sent from django"
        message="Hey yah!!!!"
        email_from=settings.EMAIL_HOST_USER
        recipient_list=['gffsg@gmail.com']
        send_mail(subject, message, email_from, recipient_list)"""
        return redirect('/login')
    else:

        return render(request, 'expense/signup.html')
def search(request):
    if request.method=='POST':
        text=request.POST.get('search')
        search = spent.objects.all().filter(spent_on=text)
        amount_sum=spent.objects.all().filter(spent_on=text).aggregate(Sum('amount')).get('amount__sum', 0.00)
        template = loader.get_template('expense/index.html')
        context = {
            'latest_question_list': search,
            'amount_sum': amount_sum,
        }
        
        return HttpResponse(template.render(context, request))
def login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('/login')

    else:
        return render(request, 'expense/login.html')



def logout(request):
    auth.logout(request)
    return redirect('/login')

class SpentViewSet(viewsets.ModelViewSet):
    queryset=spent.objects.all().filter(user_name='9')
    serializer_class=Spent_serializer
    permission_classes=(
        permissions.IsAuthenticatedOrReadOnly,
        )


class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=User_serializer
    permission_classes=(
        permissions.IsAuthenticatedOrReadOnly,
        )
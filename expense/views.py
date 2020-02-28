from django.shortcuts import render, redirect
from django.template import loader
from . models import spent, User
import datetime
from django.db.models import Sum
from .forms import Add_form
# Create your views here.


from django.http import HttpResponse
from . models import spent


def index(request):
    if request.method == 'POST':
        a=spent()
        a.user_name_id=1
        a.spent_on=request.POST.get('spent_on')
        a.reason=request.POST.get('reason')
        a.amount=request.POST.get('amount')
        a.time=datetime.datetime.now()
        a.save()
       
            
        return redirect('/')
        
    else:
        latest_question_list = spent.objects.filter(user_name='1')
        amount_sum=spent.objects.all().aggregate(Sum('amount')).get('amount__sum', 0.00)
        template = loader.get_template('expense/index.html')
        context = {
            'latest_question_list': latest_question_list,
            'amount_sum': amount_sum,
        }
        
        return HttpResponse(template.render(context, request))
    
def new_index(request, question_id):
    new=spent.objects.filter(id=question_id).delete()
    print(new)
    return redirect("/")

def signup(request):
    if request.method=="POST":
        b=User()
        b.username=request.POST.get('username')
        b.password=request.POST.get('password1')
        b.save()
        return redirect('/')   
    else:
        return render(request, 'expense/signup.html')
    
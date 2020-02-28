from django.contrib import admin
from django.urls import path
from . import views

app_name = 'expense'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.new_index, name='index_two'),
    path('signup', views.signup, name='signup'),
]

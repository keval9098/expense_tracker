from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'expense'

router = routers.DefaultRouter()
router.register('expense', views.SpentViewSet)
router.register('userr', views.UserViewSet)
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.new_index, name='index_two'),
    path('signup', views.signup, name='signup'),
    path('search', views.search, name='search'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('api', include(router.urls), name='api'),
    
    
]

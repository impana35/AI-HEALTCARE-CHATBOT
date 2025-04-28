from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Admin_login/', views.Admin_login, name='Admin_login'),
    path('User_login/', views.User_login, name='User_login'),
    path('Register/', views.Register, name='Register'),  
    path('logout/', views.logout, name='logout'), 
    path('ManageHospital/', views.ManageHospital, name='ManageHospital'),  
    path('ManageDoctor/', views.ManageDoctor, name='ManageDoctor'), 
    path('ViewUser/', views.ViewUser, name='ViewUser'), 
    path('HospitalDetails/', views.HospitalDetails, name='HospitalDetails'), 
    path('DoctorDetails/', views.DoctorDetails, name='DoctorDetails'),
    path('Chatpage/', views.Chatpage, name='Chatpage'),  
    path('Chatreply/', views.Chatreply, name='Chatreply'),  
    path('TrainingData/', views.TrainingData, name='TrainingData'),  
]

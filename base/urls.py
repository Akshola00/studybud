from django.urls import path
from . import views

urlpatterns = [

    path('login', views.loginpage, name="login"),
    path('inner_register', views.regpage, name="inner_register"),

    path('logout', views.logoutuser, name="logout"),

    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),
    
    path('create-room/', views.CreateRoom, name="create-room"),
    path('update-room/<str:pk>/', views.UpdateRoom, name="update-room"),
    path('delete-room/<str:pk>/', views.DeleteRoom, name="delete-room"),
    path('delete-message/<str:pk>/', views.DeleteMessage, name="delete-message"),
   
    path('update-user', views.updateUser, name="update-user"),

    path('topics/', views.topicsPage, name="topics"),
    path('activity/', views.activityPage, name="activity"),
]
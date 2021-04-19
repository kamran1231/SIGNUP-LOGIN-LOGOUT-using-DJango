
from django.contrib import admin
from django.urls import path
from enroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.sign_up,name='signup'),
    path('login/', views.user_login,name='login'),
    path('profile/', views.user_profile,name='profile'),
    path('logout/', views.user_logout,name='logout'),
    path('changepsw/', views.change_password,name='changepsw'),
    path('forgetpsw/', views.forget_password,name='forgetpsw'),
    path('userdetail/<int:pk>', views.user_detail,name='userdetail'),
]

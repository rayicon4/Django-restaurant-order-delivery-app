from django.urls import path
from .views import (home, register,logins, logoutuser, menu, about, 
contact, gallery, dashboard, dashboardupdate, customerdatabase, 
morningmenudelete, updatemenuitem, updatemenuafternoon, updatemenuevening, 
afternoonmenudelete, eveningmenudelete, orderpagemorning, menuordermorning, dashboardentry)



urlpatterns = [
    path('', home, name = 'home'),
    path('register/', register, name='register'),
    path('logins/', logins, name='logins'),
    path('logoutuser/', logoutuser, name='logoutuser'),
    path('menu/', menu, name='menu'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('gallery/', gallery, name='gallery'),
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboardupdate/', dashboardupdate, name='dashboardupdate'),
    path('customerdatabase/', customerdatabase, name='customerdatabase'),
    path('morningmenudelete/<str:pk>/', morningmenudelete, name='morningmenudelete'),
    path('afternoonmenudelete/<int:pk>/', afternoonmenudelete, name='afternoonmenudelete'),
    path('eveningmenudelete/<int:pk>/', eveningmenudelete, name='eveningmenudelete'),
    path('updatemenuitem/<int:pk>/', updatemenuitem, name='updatemenuitem'),
    path('updatemenuafternoon/<int:pk>/', updatemenuafternoon, name='updatemenuafternoon'),
    path('updatemenuevening/<int:pk>/', updatemenuevening, name='updatemenuevening'),
    path('orderpagemorning/<int:pk>/', orderpagemorning, name='orderpagemorning'),
    path('menuordermorning/<int:pk>/', menuordermorning, name='menuordermorning'),
    path('dashboardentry/', dashboardentry, name='dashboardentry'),
    #path('system/', system, name='system'),
]
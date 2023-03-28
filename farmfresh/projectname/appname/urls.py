from django.urls import path
from . import views
urlpatterns= [
    path('',views.index,name='index'),
    path('j',views.functionname, name='functionname'),
    path('k',views.ind,name='k'),
    path("register",views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout, name="logout")

]




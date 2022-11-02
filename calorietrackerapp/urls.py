from django.urls import path

from . import views

urlpatterns = [
    path('', views.login_v, name='index'), #DONE
    #path('', views.index, name='index'),
    path('login', views.login_v, name='login'), #DONE
    path('logout', views.logout_v, name='logout'), #DONE
    path('register', views.register, name='register'), #DONE
    path('food/list', views.foodlist, name='food_list'),
    path('food/add', views.foodadd, name='food_add'),

]
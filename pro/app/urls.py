from django.urls import path
from app import views

urlpatterns =[
    path('',views.index),
    path('signup/',views.signup),
    path('login/',views.login),
    path('loign_check/',views.loign_check),
    path('table/',views.table),
    path('delete/<int:uid>/',views.delete),
    path('update/<int:uid>/',views.update),
    path('upd/',views.update_check),
]

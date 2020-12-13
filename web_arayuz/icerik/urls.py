from django.contrib import admin
from django.urls import path
from . import views

app_name = "icerik"

urlpatterns = [
    path('',views.girisler_index,name='index'),
    path('kisi_detay/<int:id>',views.kisi_detay),
    path('giris_iptal/',views.girisler_iptal),
]
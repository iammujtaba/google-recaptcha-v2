from django.urls import path
from recaptchav2 import views

urlpatterns = [
    path("",views.index,name="index"),
    path("confirmed/",views.confirmed_captcha,name="confirmed")
]
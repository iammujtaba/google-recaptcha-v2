import requests
import logging
from django.shortcuts import render
from django.http.response import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

logger = logging.getLogger("app")
@csrf_exempt
def index(request):
    if request.method =="POST":
        client_captcha_resp = request.POST.get('g-recaptcha-response')
        url = settings.GOOGLE_RECPATCHA_URL
        values = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': client_captcha_resp
        }
        resp  = requests.post(url,data=values).json()

        if resp['success'] == False:
            print(f"Captcha failed due to {resp['error-codes']}")
            return HttpResponseRedirect("/captcha/")

        print("Captcha verification passed")
        return HttpResponseRedirect("confirmed/")
    return render(request,"index.html")


def confirmed_captcha(request):
    return render(request,"confirmed.html")
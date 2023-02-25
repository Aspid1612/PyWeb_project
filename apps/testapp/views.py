from django.shortcuts import render


from django.views import View
from django.http import HttpResponse
from random import random
# Create your views here.

class Random_View(View):
    def get(self, requests):
        random_number = random()
        return HttpResponse(random_number)
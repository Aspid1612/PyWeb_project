from django.shortcuts import render

from django.views import View
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


# @csrf_exempt
class LoginView(View):
    def get(self, request):
        return render(request, 'auth_shop/index.html')

    def post(self, request):
        return JsonResponse(request.POST, json_dumps_params={'indent': 4})

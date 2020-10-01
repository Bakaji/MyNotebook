from django.contrib import admin
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import path, include, re_path
from rest_framework.views import APIView


class Home(APIView):
    @staticmethod
    def get(request, redirect_path=None):
        if request.user.is_authenticated:
            if redirect_path:
                return render(request, 'home.html', {"redirect_to": redirect_path})
            else:
                return render(request, 'home.html')
        else:
            return redirect('/login/')


class Login(APIView):
    @staticmethod
    def get(request: HttpRequest):
        if not request.user.is_authenticated:
            return render(request, 'login.html')
        else:
            return redirect(request.path)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('login/', Login.as_view()),
    re_path(r'^$', Home.as_view()),
    re_path(r'^(?P<redirect_path>.*)/$', Home.as_view()),
]

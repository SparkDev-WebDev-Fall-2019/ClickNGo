"""ClicknGo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),

    # Our project urls
    path('', include('StorePage.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='Users/login.html'), name='login'), # handle logins
    path('logout/', auth_views.LogoutView.as_view(template_name='StorePage/_base.html'), name='logout'), # redirect logouts to front page
    path('', include('Users.urls', namespace='profile_settings')), # Users/Profile urls
    path('Questions/', include('Questions.urls')), # Questions Urls
    path('Communities', include('Communities.urls')),
    path('', include('social_django.urls', namespace='social'))
]

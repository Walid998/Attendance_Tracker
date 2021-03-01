"""OurCompany URL Configuration

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
from django.urls import path
from django.urls.conf import include
from Accounts.views import forbeddin, home,manager_home,employee_home,employees_requests

urlpatterns = [
    path('', home),
    path('Home/',employee_home,name="Home"),
    path('Dashboard/',manager_home,name="Dashboard"),
    path('Requests/',employees_requests,name="Requests"),
    path('forbeddin/',forbeddin,name="forbeddin"),
    path('admin/', admin.site.urls),
    path('accounts/',include("django.contrib.auth.urls")),
    path('api/Accounts/',include("Accounts.api.urls","Accounts_api"))
    
]

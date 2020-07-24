"""reminder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from services.views import *
from authentication.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name="home"),

    path('login/', login_view, name="login"),
    path('signup/', signup_view, name="signup"),

    path('service/', service_view, name="service"),
    path('service/incometax/', incometax_view, name="incometax"),
    path('service/gst/', gst_view, name="gst"),
    path('service/companies_act/', companies_act_view, name="companies_act"),
    path('service/accounting/', accounting_view, name="accounting"),

    # path('service/<slug:username>/', service_view, name='service'),
    path('profile/', profile_view, name='profile'),

    path('logout/', logout_view, name="logout"),
    path('aboutus/', aboutus_view, name="aboutus"),
    path('team/', team_view, name="team"),
    # path('signup/', signup_view, name="signup"),
    # path('sent/', activation_sent_view, name="activation_sent"),
    # path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),
]

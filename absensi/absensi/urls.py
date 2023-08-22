"""
URL configuration for absensi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from . import views
from biodata.views import *
from perizinan.views import *
from presensi.views import *

urlpatterns = [
    # Route untuk Biodata
    path('admin/', admin.site.urls),
    path('', views.index),

    # CRUD Biodata
    path('biodata/', views.data),
    path('tambahbd/',tambahdt),
    path('ubahdt/',ubahdt),
    path('hapusdt/',hapusdt),

    # CRUD Perizinan
    path('perizinan/',views.perizinan),
    # path('tambahizn/',tambahizn),
    # path('ubahizn/',ubahizn),
    # path('hapusizn/',hapusizn),

    # CRUD Laporan
    path('laporan/',views.laporan),
    # path('cetaklpr',views.cetaklpr),
    

]

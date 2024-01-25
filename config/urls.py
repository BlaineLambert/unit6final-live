"""
URL configuration for config project.

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from app import views
from config import settings

urlpatterns = [
    path('booking/<str:name>', views.booking, name='booking'),
    path('filter-search/<item>/', views.filter, name="filter"),
    path('logout/', views.logout_func),
    path('register/', views.register, name='register'),
    path('login/', views.loginpage, name='login'),
    path('admin/', admin.site.urls),
    path('', views.homepage, name='home'),
    path('userpage/', views.userpage, name='user'),
    path('property/', views.add_property, name='property')
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

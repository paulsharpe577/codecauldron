"""
URL configuration for django_portfolio project.

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from register import views as v

from machina import urls as machina_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),  # new
    path("", include("pages.urls")),
    path("projects/", include("projects.urls")),
    path("walkthroughs/", include("blog.urls")), #NEW
    path('forum/', include(machina_urls)),
    path("register/", v.register, name="register"),  # <-- added
    path("accounts/", include("django.contrib.auth.urls")),  # new
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

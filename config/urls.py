"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from dj_rest_auth.views import PasswordResetConfirmView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Book Review API",
        default_version="v1",
        description="A simple API for Book Review",
        terms_of_service="",
        contact=openapi.Contact(email="afsharzadeh1998@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/book/', include('books.urls', namespace='books')),
    path('api/comment/', include('comments.urls', namespace='comments')),

    path('api/account/', include('dj_rest_auth.urls')),
    path('api/account/registration/', include('dj_rest_auth.registration.urls')),
    path('api/account/password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

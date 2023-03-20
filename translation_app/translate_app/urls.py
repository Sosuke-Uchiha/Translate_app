from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import (add_project, dashboard, project, register_request, login_request, logout_request)

urlpatterns = [
    path('add_project/', add_project, name='add_project'),
    path('', dashboard, name='dashboard'),
    path('project/<int:id>', project, name='project'),
    path("register", register_request, name="register"),
    path("login", login_request, name="login"),
    path("logout", logout_request, name= "logout"),


] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

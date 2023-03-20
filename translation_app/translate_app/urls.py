from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import (add_project, dashboard, project)

urlpatterns = [
    path('add_project/', add_project, name='add_project'),
    path('', dashboard, name='dashboard'),
    path('project/<int:id>', project, name='project')
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

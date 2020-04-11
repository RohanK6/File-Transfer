from django.urls import path
from . import views
from FileTransfer import settings 
from django.conf.urls.static import static 

urlpatterns = [
    path('', views.index, name='index'),
    path('/upload', views.upload, name='upload'),
    path('/success', views.success, name='success'),
    path('/download', views.download, name='download')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
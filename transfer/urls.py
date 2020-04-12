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

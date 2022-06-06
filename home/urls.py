from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings
app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
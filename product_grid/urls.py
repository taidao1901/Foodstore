from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings

urlpatterns = [
    path('<slug:filter>', views.product_grid, name='product_grid'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
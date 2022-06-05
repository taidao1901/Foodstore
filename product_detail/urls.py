from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings

urlpatterns = [
    path('<slug:product>', views.product_detail, name="product_detail"),
]+static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
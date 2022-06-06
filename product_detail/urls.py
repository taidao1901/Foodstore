from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings
app_name= 'product_detail'
urlpatterns = [
    path('<slug:product>', views.product_detail, name= 'prod_detail'),
]+static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
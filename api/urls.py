from django.urls import path
from .views import CompanyView

urlpatterns = [
    path('companies/',CompanyView.as_view(), name='companies_list'),
    path('companies/<int:id>',CompanyView.as_view(), name='companies_process') # Esta url sirve para que reciba y este preparada para buscar por id mediante el GET, eliminar mediante el DELETE y actualizar mediante el PUT.
]
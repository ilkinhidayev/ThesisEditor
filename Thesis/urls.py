from django.urls import path
from . import views

urlpatterns = [
    path('tez-yukle/', views.tez_yukle, name='tez_yukle'),
    path('tez-listesi/', views.tez_listesi, name='tez_listesi'),
    path('delete-tez/<int:tez_id>/', views.delete_tez, name='delete_tez'),

]

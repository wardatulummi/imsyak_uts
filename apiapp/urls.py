from django.urls import path
from . import views 

app_name='apiapp'

urlpatterns = [
#fbv1
path('',views.readjadwal),
path('alamat/<int:id>', views.detailjadwal),
path('buat/', views.createjadwal),
path('edit/int:id>', views.updatejadwal),
path('hapus/int:id', views.deletejadwal),  
]
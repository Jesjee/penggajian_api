from django.urls import path
from .views import KaryawanList, KaryawanDetail, PenggajianList, PenggajianDetail

urlpatterns = [
    path('karyawan/', KaryawanList.as_view()),
    path('karyawan/<int:pk>/', KaryawanDetail.as_view()),
    path('penggajian/', PenggajianList.as_view()),
    path('penggajian/<int:pk>/', PenggajianDetail.as_view()),
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import KaryawanViewSet, PenggajianViewSet

router = DefaultRouter()
router.register(r'karyawan', KaryawanViewSet)
router.register(r'penggajian', PenggajianViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
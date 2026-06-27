from rest_framework import viewsets
from .models import Karyawan, Penggajian
from .serializers import KaryawanSerializer, PenggajianSerializer

class KaryawanViewSet(viewsets.ModelViewSet):
    queryset = Karyawan.objects.all()
    serializer_class = KaryawanSerializer

class PenggajianViewSet(viewsets.ModelViewSet):
    queryset = Penggajian.objects.all()
    serializer_class = PenggajianSerializer
from rest_framework import viewsets, filters
from .models import Karyawan, Penggajian
from .serializers import KaryawanSerializer, PenggajianSerializer

class KaryawanViewSet(viewsets.ModelViewSet):
    queryset = Karyawan.objects.all()
    serializer_class = KaryawanSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nama', 'jabatan', 'departemen']
    ordering_fields = ['nama', 'jabatan']

class PenggajianViewSet(viewsets.ModelViewSet):
    queryset = Penggajian.objects.all()
    serializer_class = PenggajianSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['karyawan__nama']
    ordering_fields = ['bulan', 'tahun', 'total_gaji']
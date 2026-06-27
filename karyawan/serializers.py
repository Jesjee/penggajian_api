from rest_framework import serializers
from .models import Karyawan, Penggajian

class KaryawanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Karyawan
        fields = '__all__'

class PenggajianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Penggajian
        fields = '__all__'
        read_only_fields = ['total_gaji']
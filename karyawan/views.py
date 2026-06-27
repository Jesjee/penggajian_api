from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Karyawan, Penggajian
from .serializers import KaryawanSerializer, PenggajianSerializer

class KaryawanList(APIView):
    def get(self, request):
        karyawan = Karyawan.objects.all()
        serializer = KaryawanSerializer(karyawan, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = KaryawanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class KaryawanDetail(APIView):
    def get_object(self, pk):
        try:
            return Karyawan.objects.get(pk=pk)
        except Karyawan.DoesNotExist:
            return None

    def get(self, request, pk):
        obj = self.get_object(pk)
        if obj is None:
            return Response({'error': 'Tidak ditemukan'}, status=status.HTTP_404_NOT_FOUND)
        serializer = KaryawanSerializer(obj)
        return Response(serializer.data)

    def put(self, request, pk):
        obj = self.get_object(pk)
        if obj is None:
            return Response({'error': 'Tidak ditemukan'}, status=status.HTTP_404_NOT_FOUND)
        serializer = KaryawanSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        obj = self.get_object(pk)
        if obj is None:
            return Response({'error': 'Tidak ditemukan'}, status=status.HTTP_404_NOT_FOUND)
        serializer = KaryawanSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        obj = self.get_object(pk)
        if obj is None:
            return Response({'error': 'Tidak ditemukan'}, status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PenggajianList(APIView):
    def get(self, request):
        penggajian = Penggajian.objects.all()
        serializer = PenggajianSerializer(penggajian, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PenggajianSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PenggajianDetail(APIView):
    def get_object(self, pk):
        try:
            return Penggajian.objects.get(pk=pk)
        except Penggajian.DoesNotExist:
            return None

    def get(self, request, pk):
        obj = self.get_object(pk)
        if obj is None:
            return Response({'error': 'Tidak ditemukan'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PenggajianSerializer(obj)
        return Response(serializer.data)

    def put(self, request, pk):
        obj = self.get_object(pk)
        if obj is None:
            return Response({'error': 'Tidak ditemukan'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PenggajianSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        obj = self.get_object(pk)
        if obj is None:
            return Response({'error': 'Tidak ditemukan'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PenggajianSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        obj = self.get_object(pk)
        if obj is None:
            return Response({'error': 'Tidak ditemukan'}, status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
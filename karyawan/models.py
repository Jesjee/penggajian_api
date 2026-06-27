from django.db import models

class Karyawan(models.Model):
    nama = models.CharField(max_length=100)
    jabatan = models.CharField(max_length=100)
    departemen = models.CharField(max_length=100)

    def __str__(self):
        return self.nama

class Penggajian(models.Model):
    karyawan = models.ForeignKey(Karyawan, on_delete=models.CASCADE, related_name='penggajian')
    bulan = models.IntegerField()
    tahun = models.IntegerField()
    gaji_pokok = models.DecimalField(max_digits=12, decimal_places=2)
    tunjangan = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_gaji = models.DecimalField(max_digits=12, decimal_places=2, blank=True)

    def save(self, *args, **kwargs):
        self.total_gaji = self.gaji_pokok + self.tunjangan
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.karyawan.nama} - {self.bulan}/{self.tahun}"
from django.db import models
#from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from django_resized import ResizedImageField 


class Kategori(models.Model):
    nama = models.CharField(max_length=200, blank=True, null=False)
    aktif = models.BooleanField(default= True)
    banner_satu = ResizedImageField(size=[575, 200], quality=80, crop=['middle', 'center'] , upload_to='gambar/banner', blank=True, null=True, verbose_name="BANNER SATU")
    banner_dua = ResizedImageField(size=[575, 200], quality=80, crop=['middle', 'center'] , upload_to='gambar/banner', blank=True, null=True, verbose_name="BANNER DUA")
    slug = models.SlugField(max_length=200, null=True,blank=True, unique=True)
    class Meta:
        verbose_name_plural ="Data Kategori"

    def __str__(self):
        return f"Nama: {self.nama}"
    
    
    @property
    def get_produk(self):
        return Produk.objects.filter(kategori__slug=self.slug)



class Produk(models.Model):
    KETERANGAN=(
        ('Baru', 'Baru'),
        ('Lama' , 'Lama'),
    )
    kategori = models.ForeignKey(Kategori, null=True, blank=True, related_name="produks", on_delete=models.SET_NULL)
    nama_produk = models.CharField(max_length=200, blank=True, null=True)
    
    gambar = ResizedImageField(size=[270, 250], quality=80, crop=['middle', 'center'] , upload_to='gambar/banner', blank=False, null=True, verbose_name="Gambar 1")
    gambar_satu = ResizedImageField(size=[270, 250], quality=80, crop=['middle', 'center'] , upload_to='gambar/banner', blank=True, null=True, verbose_name="Gambar 2")
    gambar_dua = ResizedImageField(size=[270, 250], quality=80, crop=['middle', 'center'] , upload_to='gambar/banner', blank=True, null=True, verbose_name="Gambar 3")
    gambar_tiga = ResizedImageField(size=[270, 250], quality=80, crop=['middle', 'center'] , upload_to='gambar/banner', blank=True, null=True, verbose_name="Gambar 4")
    gambar_empat = ResizedImageField(size=[270, 250], quality=80, crop=['middle', 'center'] , upload_to='gambar/banner', blank=True, null=True, verbose_name="Gambar 5")
    gambar_lima = ResizedImageField(size=[270, 250], quality=80, crop=['middle', 'center'] , upload_to='gambar/banner', blank=True, null=True, verbose_name="Gambar 6")
    slug = models.SlugField(max_length=200, unique=True)
    keterangan = RichTextField(blank=True, null=True)
    harga = models.PositiveIntegerField(blank=True, null=True)
    no_whatsup = models.PositiveBigIntegerField(blank=True, null=True,)
    tanggal_upload= models.DateTimeField(auto_now_add=True, null=True)
    diskon = models.IntegerField(default=0, blank=True, null=True)
    dibeli = models.IntegerField(default=0, blank=True, null=True)
    keterangan_barang = models.CharField(max_length=200, null=True, choices=KETERANGAN)
    class Meta:
        verbose_name_plural ="Produk"
    def __str__(self):
        return self.nama_produk

    @property
    def setelah_diskon(self):
        if self.diskon == 0 :
            nilai_diskon = self.harga
        else:
            jml = self.diskon / 100
            nilai_diskon = self.harga - (jml * self.harga)
        return nilai_diskon




class Slide(models.Model):
    teks_awal = models.CharField(max_length=200, blank=True, null=True)
    teks_dua = models.CharField(max_length=200, blank=True, null=True)
    teks_tiga = models.CharField(max_length=200, blank=True, null=True)
    gambar_slide = ResizedImageField(size=[880, 475], quality=80, crop=['middle', 'center'] , upload_to='gambar/slide', blank=False, null=True, verbose_name="Gambar Slide")
    aktif = models.BooleanField(default=True)
    class Meta:
        verbose_name_plural ="Slide"



class Kontak(models.Model):
    nama = models.CharField(max_length=200, blank=False, null=True)
    no_whatsup = models.PositiveBigIntegerField(blank=True, null=True,)
    email = models.EmailField(max_length=200,blank=False, null=True)
    subject = models.CharField(max_length=200, blank=False, null=True)
    isi = models.TextField(max_length=200, blank=False, null=True)
    class Meta:
        verbose_name_plural ="Kontak"

class Profil(models.Model):
    nama = models.CharField(max_length=200, blank=False, null=True)
    keterangan = RichTextField(blank=True, null=True)
    gambar = ResizedImageField(size=[1920, 1200], quality=80, crop=['middle', 'center'] , upload_to='gambar/profil', blank=False, null=True, verbose_name="Gambar")
    tanggal_upload= models.DateTimeField(auto_now_add=True, null=True)
    class Meta:
        verbose_name_plural ="Profil"



class Statis(models.Model):
    alamat_kami = models.TextField(max_length=200, blank=False, null=True)
    telpon = models.CharField(max_length=200, blank=False, null=True)
    email = models.EmailField(max_length=200, blank=False, null=True)
    class Meta:
        verbose_name_plural ="Statis"


class ChatID(models.Model):
    chatid = models.CharField(max_length=200, blank=False, null=True)
    nama = models.CharField(max_length=200, blank=False, null=True)
    aktif = models.BooleanField(default= True)
    class Meta:
        verbose_name_plural ="Data Chat ID"

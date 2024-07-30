from django.contrib import admin
from .models import Kategori, Produk, Slide, Kontak, Profil, Statis, ChatID

class DataKategoriAdmin(admin.ModelAdmin):
    list_display = ("nama", "aktif", "banner_satu", "banner_dua",)
    prepopulated_fields = {"slug": ("nama",)} 

class DataProdukAdmin(admin.ModelAdmin):
    list_display = ("kategori","nama_produk", "gambar","harga","diskon","dibeli","keterangan_barang",)
    prepopulated_fields = {"slug": ("nama_produk",)}

class SlideAdmin(admin.ModelAdmin):
    list_display = ("teks_awal", "teks_dua", "teks_tiga","gambar_slide", "aktif",)

class KontakAdmin(admin.ModelAdmin):
    list_display = ("nama","no_whatsup","email","subject","isi",)

class ProfilAdmin(admin.ModelAdmin):
    list_display = ("nama","gambar","tanggal_upload",)

class StatisAdmin(admin.ModelAdmin):
    list_display = ("alamat_kami","telpon","email",)

class ChatidAdmin(admin.ModelAdmin):
    list_display =("nama","chatid","aktif",)


admin.site.register(Kategori,DataKategoriAdmin)
admin.site.register(Produk,DataProdukAdmin)
admin.site.register(Slide,SlideAdmin)
admin.site.register(Kontak,KontakAdmin)
admin.site.register(Profil,ProfilAdmin)
admin.site.register(Statis,StatisAdmin)
admin.site.register(ChatID,ChatidAdmin)
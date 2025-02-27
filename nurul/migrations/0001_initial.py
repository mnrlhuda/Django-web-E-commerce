# Generated by Django 4.2.7 on 2023-11-23 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(blank=True, max_length=200)),
                ('aktif', models.BooleanField(default=True)),
                ('banner_satu', models.ImageField(null=True, upload_to='gambar/banner')),
                ('banner_dua', models.ImageField(null=True, upload_to='gambar/banner')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Kontak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200, null=True)),
                ('no_whatsup', models.PositiveBigIntegerField(blank=True, null=True)),
                ('email', models.EmailField(max_length=200, null=True)),
                ('subject', models.CharField(max_length=200, null=True)),
                ('isi', models.TextField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200, null=True)),
                ('keterangan', models.TextField(blank=True, max_length=200, null=True)),
                ('gambar', models.ImageField(null=True, upload_to='gambar/profil', verbose_name='Gambar (1920 x 1200 pixel)')),
                ('tanggal_upload', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teks_awal', models.CharField(blank=True, max_length=200, null=True)),
                ('teks_dua', models.CharField(blank=True, max_length=200, null=True)),
                ('teks_tiga', models.CharField(blank=True, max_length=200, null=True)),
                ('gambar_slide', models.ImageField(null=True, upload_to='gambar/slide')),
                ('aktif', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Statis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alamat_kami', models.TextField(max_length=200, null=True)),
                ('telpon', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_produk', models.CharField(blank=True, max_length=200, null=True)),
                ('gambar', models.ImageField(null=True, upload_to='gambar/banner')),
                ('gambar_satu', models.ImageField(null=True, upload_to='gambar/banner')),
                ('gambar_dua', models.ImageField(null=True, upload_to='gambar/banner')),
                ('gambar_tiga', models.ImageField(null=True, upload_to='gambar/banner')),
                ('gambar_empat', models.ImageField(null=True, upload_to='gambar/banner')),
                ('gambar_lima', models.ImageField(null=True, upload_to='gambar/banner')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('keterangan', models.TextField(blank=True, max_length=200, null=True)),
                ('harga', models.PositiveIntegerField(blank=True, null=True)),
                ('no_whatsup', models.PositiveBigIntegerField(blank=True, null=True)),
                ('tanggal_upload', models.DateTimeField(auto_now_add=True, null=True)),
                ('diskon', models.IntegerField(blank=True, default=0, null=True)),
                ('dibeli', models.IntegerField(blank=True, default=0, null=True)),
                ('keterangan_barang', models.CharField(choices=[('Baru', 'Baru'), ('Lama', 'Lama')], max_length=200, null=True)),
                ('kategori', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='produks', to='nurul.kategori')),
            ],
        ),
    ]

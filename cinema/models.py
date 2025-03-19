from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Kategoriya')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Kategoeiya'
        verbose_name_plural = 'Kategoriyalar'


class Cinema(models.Model):
    title = models.CharField(max_length=255, verbose_name='Film nomlari')
    context = models.TextField(verbose_name='Film xaqida')
    photo = models.ImageField(upload_to='photos/', null=True, blank=True, verbose_name="Foto")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')
    updated_ad = models.DateTimeField(auto_now=True, verbose_name='Yangilangan vaqti')
    views = models.IntegerField(default=0, verbose_name='K\'rishlar soni')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    video = models.CharField(max_length=255, verbose_name='Ssilka video', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Aftor')

    def __str__(self):
        return self.title

    def get_photo_cinema(self):
        try:
            return self.photo.url
        except:
            return 'https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava3.webp'

    def get_absolute_url(self):
        return reverse('cinema', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Film'
        verbose_name_plural = 'Filmlar'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Kommentchi')
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, verbose_name='Film')
    text = models.TextField(verbose_name='Kommentariya')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Kommentariya'
        verbose_name_plural = 'Kommentariyalar'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Foydalanuvchi')
    photo = models.ImageField(upload_to='profiles/', blank=True, null=True, verbose_name='Profil fotosi')
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name='Telefon raqami')
    about_user = models.CharField(max_length=100, blank=True, null=True, verbose_name='Foydalanuvchi xaqida')
    publisher = models.BooleanField(default=True, verbose_name='Filmga ruxsat')

    def __str__(self):
        return self.user.username

    def get_photo_user(self):
        try:
            return self.photo.url
        except:
            return 'https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava3.webp'

    class Meta:
        verbose_name = 'Profil'
        verbose_name_plural = 'Profils'

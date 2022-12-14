from django.db import models
from django import forms


def change_html(url):
    with open('../templates/include/logo-tag.html', 'w') as template:
        template.write(f'<img src="{url}" alt="logo">')

# Create your models here.

class HomeImage(models.Model):
    image = models.ImageField(upload_to='images/home_image')

    def clean(self):
        if len(HomeImage.objects.all()) >= 1:
            raise forms.ValidationError("you can't have more than 1 image")

    def save(self, *args, **kwargs):
        if len(HomeImage.objects.all()) >= 1:
            raise models.RestrictedError("you can't have more than 1 image", self)
        super().save(*args, **kwargs)


class LogoImage(models.Model):
    image = models.ImageField(upload_to='images/logo_image')

    def clean(self):
        if len(LogoImage.objects.all()) >= 1:
            raise forms.ValidationError("you can't have more than 1 image")

    def save(self, *args, **kwargs):
        if len(LogoImage.objects.all()) >= 1:
            raise models.RestrictedError("you can't have more than 1 image", self)

        super().save(*args, **kwargs)
        change_html(self.image.url)


class AboutImage(models.Model):
    image = models.ImageField(upload_to='images/about_image')

    def clean(self):
        if len(AboutImage.objects.all()) >= 1:
            raise forms.ValidationError("you can't have more than 1 image")

    def save(self, *args, **kwargs):
        if len(AboutImage.objects.all()) >= 1:
            raise models.RestrictedError("you can't have more than 1 image", self)
        super().save(*args, **kwargs)

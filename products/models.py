from django.db import models
from django.utils.text import slugify
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse_lazy


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, db_index=True, editable=False)
    description = models.TextField()
    image = models.ImageField()
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    old_price = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0.0)])

    @property
    def url(self):
        return reverse_lazy('product', self.slug)

    def __str__(self):
        return f'{self.name}'

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.name)
        super(Product, self).save(force_insert, force_update, using, update_fields)

    def clean(self):
        slug = slugify(self.name)
        try:
            Product.objects.get(slug=slug)  # raise error when nothing found (new slug)
            try:
                Product.objects.get(id=self.id)  # raise error when uuid not in db (new entity)
            except Product.DoesNotExist:
                # only if the slug is old
                # and the entity is new
                raise forms.ValidationError({'title': "this name can't be slugified because it is used before"})
        except Product.DoesNotExist:
            pass


class Invoice(models.Model):
    # class Meta:
    #     unique_together = (('id', 'product'),)

    products = models.ManyToManyField(Product, related_name='invoices')
    confirmed = models.BooleanField()   # if false that means its temporary
    delivered = models.BooleanField()

    @property
    def total_price(self):
        return Invoice.objects.produ

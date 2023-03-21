from django.db import models
from django.utils.text import slugify
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Item(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, db_index=True, editable=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    description = models.TextField()
    image = models.ImageField()
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    old_price = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0.0)])

    def __str__(self):
        return f'{self.name} from {self.category.name}'

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.name)
        super(Item, self).save(force_insert, force_update, using, update_fields)

    def clean(self):
        slug = slugify(self.name)
        try:
            Item.objects.get(slug=slug)  # raise error when nothing found (new slug)
            try:
                Item.objects.get(id=self.id)  # raise error when uuid not in db (new entity)
            except Item.DoesNotExist:
                # only if the slug is old
                # and the entity is new
                raise forms.ValidationError({'title': "this name can't be slugified because it is used before"})
        except Item.DoesNotExist:
            pass

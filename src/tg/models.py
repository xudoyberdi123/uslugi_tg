from django.db import models

# Create your models here.
from django.db.models import JSONField
from mptt.fields import TreeForeignKey
from mptt.managers import TreeManager
from mptt.models import MPTTModel

from base.fields import default_salary
from geo.models import Region
from tg import default_log, lang_dict_field, create_slug


class Log(models.Model):
    user_id = models.BigIntegerField(primary_key=True, null=False)
    messages = models.JSONField(blank=True, null=True, default=default_log())

    def __str__(self):
        return "#%s" % self.user_id


class User(models.Model):
    user_id = models.BigIntegerField(primary_key=True, null=False)
    user_name = models.CharField(max_length=256, null=True)
    first_name = models.CharField(max_length=256, null=False)
    last_name = models.CharField(max_length=256, null=True)
    lang = models.IntegerField(null=True)
    menu_log = models.IntegerField(null=True)


# class Languages(models.Model):
#     name = JSONField(blank=False, null=False, default=lang_dict_field())
#     alias = models.CharField(max_length=32, unique=True)
#     sort_order = models.IntegerField(db_index=True, null=True)
#
#     def __str__(self):
#         return self.alias


class Category(MPTTModel):
    name = JSONField(blank=False, null=False, default=lang_dict_field)
    slug = models.SlugField(unique=True, max_length=255)
    parent = TreeForeignKey('self', related_name='categories', null=True, blank=True, on_delete=models.SET_NULL)

    objects = models.Manager()
    tree = TreeManager()
    is_active = models.BooleanField(default=True)
    is_main = models.BooleanField(default=False)
    sort_order = models.IntegerField(db_index=True, null=True)

    def __str__(self):
        return self.name['ru']

    class MPTTMeta:
        order_insertion_by = ['sort_order']

    def get_ordering_queryset(self):
        return Category.objects.all()

    def save(self, *args, **kwargs):
        self.slug = create_slug(self)
        return super().save(*args, **kwargs)


class Announce(models.Model):
    fullname = models.CharField(max_length=50, null=True, blank=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=30, null=True, blank=True)
    price = models.JSONField(null=True, blank=True, default=default_salary())
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def str(self):
        return self.fullname


class AnnounceCategories(models.Model):
    resume = models.ForeignKey(
        Announce,
        related_name="announce_categories_m",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )

    category = models.ForeignKey(
        Category,
        related_name="announce_categories",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )

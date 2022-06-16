from django.db import models


class Man(models.Model):
    full_name = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.full_name


class Category(models.Model):
    title = models.CharField(max_length=100,  db_index=True)

    def __str__(self):
        return self.title
from django.db import models
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=30, default='')
    type = models.CharField(max_length=30, default='')
    location_province = models.CharField(max_length=30)
    location_town = models.CharField(max_length=30)
    description = models.TextField(max_length=None)
    qualifications = models.TextField(max_length=None)
    email = models.EmailField()
    phone_number = models.IntegerField(default=0)
    publication_date = models.DateField(auto_now_add=True)
    slug = models.SlugField(blank=True, default='')

    def __str__(self):
        return '[{}] {} {} {}'.format(self.publication_date, self.title, self.location_province, self.email)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save()

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.slug)])

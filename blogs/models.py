from django.db import models
from django.urls import reverse

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_by = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_info", kwargs={"pk": self.id})
    
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_by = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.title
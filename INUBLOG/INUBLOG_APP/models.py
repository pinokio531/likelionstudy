from django.db import models

class BlogContents(models.Model):
    title = models.CharField(max_length = 50)
    enroll_date = models.DateTimeField()
    modify_date = models.DateTimeField()
    body = models.TextField()

    def __str__(self):
        return self.title

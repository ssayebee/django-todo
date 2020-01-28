from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.title

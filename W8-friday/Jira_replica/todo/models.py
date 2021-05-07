from django.db import models

class Todo(models.Model):
    text = models.CharField(max_length=50)
    complete = models.BooleanField(default=False)

    def _str_(self):
        return self.text
    
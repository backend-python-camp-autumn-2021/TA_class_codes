from django.db import models

class Tag(models.Model):
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
    

class Product(models.Model):
    name = models.CharField(max_length=200)
    tags = models.ManyToManyField(Tag)
    
    def __str__(self) -> str:
        return self.name
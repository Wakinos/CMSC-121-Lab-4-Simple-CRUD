from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100,null=True)
    country_of_origin = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Book(models.Model):
    book_title = models.CharField(max_length=100,null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100,null=True)
    price = models.FloatField(null=True)
    number_of_pages = models.IntegerField(null=True)
    language = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.book_title + " by " + self.author.first_name + " " + self.author.last_name
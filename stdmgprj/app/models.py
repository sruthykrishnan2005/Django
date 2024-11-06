from django.db import models

# Create your models here.
class Student(models.Model):
    roll_no=models.IntegerField()
    # name=models.CharField(max_length=20)
    name=models.TextField()
    age=models.IntegerField()
    place=models.TextField()
    address=models.TextField()

    def __str__(self):
        return self.name

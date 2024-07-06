from django.db import models

# Create your models here.

class BookInfo(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name


class PeopleInfo(models.Model):
    name=models.CharField(max_length=20)
    gender=models.BooleanField()
    # 外键约束
    book=models.ForeignKey(BookInfo,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


from django.db import models


class User(models.Model):
    class Meta:
        db_table = "user"

    name = models.CharField("Name", max_length=240)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

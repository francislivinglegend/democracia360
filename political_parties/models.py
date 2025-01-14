from django.db import models

class Political_Party(models.Model):
    name = models.CharField(max_length=200)
    foundation_date = models.DateTimeField()

    def __str__(self):
        return self.name


class Deputy(models.Model):
    name = models.ForeignKey(Political_Party, max_length=200, on_delete=models.CASCADE)
    born_on = models.DateTimeField()

    def __str__(self):
        return self.name

    
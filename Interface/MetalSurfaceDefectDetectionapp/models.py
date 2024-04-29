from django.db import models

# Create your models here.


class Detection(models.Model):

    image = models.ImageField(null=False, blank=False, upload_to="predictedImages/")


    def __str__(self):
        return f"{self.image}"


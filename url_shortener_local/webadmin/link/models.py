from django.db import models

class url(models.Model):
    short_url = models.CharField(max_length=20)
    long_url = models.URLField(max_length=200)

    def dico(self):
        return {"short_url": self.short_url, "long_url": self.long_url}

    def __str__(self):
        return f"{self.short_url}"
from django.db import models


class Password(models.Model):
    password = models.TextField(max_length=15)

    def __str__(self):
        return str(self.id)


from django.db import models


class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.id)

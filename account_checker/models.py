from django.db import models

class LinkedInAccount(models.Model):
    profile_url = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

    def __str__(self):
        return self.profile_url


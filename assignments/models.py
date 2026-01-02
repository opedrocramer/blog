from django.db import models

class About(models.Model):
    heading = models.CharField(max_length=20)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'about'

    def __str__(self) -> str:
        return self.heading

class SocialLink(models.Model):
    platform = models.CharField(max_length=30)
    url = models.URLField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.platform

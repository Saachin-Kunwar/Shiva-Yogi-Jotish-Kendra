# core/models.py
from django.db import models

class Booking(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    service = models.CharField(max_length=150)
    consultation_date = models.DateField()
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.service} ({self.consultation_date})"

class GuruProfile(models.Model):
    name = models.CharField(max_length=100, default="Shiva Yogi Guru")
    title = models.CharField(max_length=200, default="Chief Astrologer & Spiritual Guide")
    bio = models.TextField(default="Welcome to Shiva Yogi Jotish Kendra. We provide authentic Vedic astrology, horoscope analysis, and spiritual healing solutions.")
    image = models.ImageField(upload_to='guru/', blank=True, null=True)

    def __str__(self):
        return self.name
from django.db import models

class Program(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    icon_class = models.CharField(max_length=50, help_text="Tailwind or FontAwesome icon name")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
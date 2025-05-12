from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    word = models.CharField(max_length=100)
    attempts_left = models.IntegerField(default=6)
    is_over = models.BooleanField(default=False)

    def __str__(self):
        return f"Game {self.id} - {self.word}"

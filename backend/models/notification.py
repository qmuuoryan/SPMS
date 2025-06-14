from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()

class Notification(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)


    def __str__(self):
        return f"To{self.user.username}: {self.message[:30]}..."
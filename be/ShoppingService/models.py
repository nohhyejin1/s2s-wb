from django.db import models

class CartInstances(models.Model):
    user_id = models.CharField(max_length=20)
    item_id = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_id, self.item_id
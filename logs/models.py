from django.db import models
from django.conf import settings

class LogsCorrida(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    distancia = models.DecimalField(max_digits=5, decimal_places=2)
    tempo = models.DecimalField(max_digits=5, decimal_places=2)
    ritmo = models.DecimalField(max_digits=5, decimal_places=2)
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.email} - {self.data}"
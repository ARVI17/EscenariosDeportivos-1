from django.db import models

# Create your models here.

class disciplina_deportivas(models.Model):
    id=models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

disciplina_deportivas
escenarios_deportivos
eventos
tipo_
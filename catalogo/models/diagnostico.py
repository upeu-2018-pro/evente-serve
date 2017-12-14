from django.db import models


class Diagnostico(models.Model):

    nombre = models.CharField(max_length=60)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE,
        related_name='diagnostico_set', null=True, blank=True
    )

    class Meta:
        verbose_name = "Diagnostico"
        verbose_name_plural = "Diagnosticos"

    def __str__(self):
        return '%s (parent: %s)' % (self.nombre, self.parent)

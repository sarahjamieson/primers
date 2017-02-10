from __future__ import unicode_literals
from django.db import models

directions = (("F", "F"), ("R", "R"))


class Primer(models.Model):
    primer_id = models.AutoField(primary_key=True)
    gene = models.CharField(max_length=10)
    exon = models.CharField(max_length=4, blank=True)
    direction = models.CharField(max_length=1, choices=directions)
    seq = models.CharField(max_length=30)

    class Meta:
        db_table = 'Primer'

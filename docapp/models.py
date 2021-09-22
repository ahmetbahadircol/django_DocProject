from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import PROTECT
from django.db.models.fields.related import ForeignKey

# Create your models here.
class DocMaster(models.Model):
    DocumentCode = models.CharField(max_length=50, primary_key=True)
    DocumentName = models.CharField(max_length=250)
    ExpDate = models.DateField()

    def __str__(self):
        return self.DocumentCode + ' ' + self.DocumentName

class DocDetail(models.Model):
    DocumentCode = models.ForeignKey(DocMaster, on_delete=PROTECT)
    Revision = models.CharField(max_length=25)
    RevDate = models.DateField()
    RevCause = models.CharField(max_length=500)

    def __str__(self):
        return self.Revision

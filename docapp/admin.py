from django.contrib import admin
from .models import DocMaster, DocDetail


# Register your models here.

admin.site.register(DocDetail)
admin.site.register(DocMaster)
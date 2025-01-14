from django.contrib import admin

# Register your models here.
from .models import Political_Party, Deputy

admin.site.register(Political_Party)
admin.site.register(Deputy)
from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Provider)
admin.site.register(Category)
admin.site.register(Resource)
admin.site.register(Contact)
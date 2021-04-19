from django.contrib import admin

# Register your models here.
from .models import Messages
from .models import Contact

admin.site.register(Messages)
admin.site.register(Contact)
from django.contrib import admin

# Register your models here.
from .models import Messages, Contact, Skill, Project, Upload

admin.site.register(Messages)
admin.site.register(Contact)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Upload)
# admin.site.register(Certification_5)
# admin.site.register(Certification_4)
# admin.site.register(Certification_3)
# admin.site.register(Certification_2)
# admin.site.register(Certification_1)
# admin.site.register(Certification_LKG)
# admin.site.register(Trophy)
# admin.site.register(Medal)


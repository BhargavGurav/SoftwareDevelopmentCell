from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header = "GCOEJ's SDC | Administration"


admin.site.register(Student)
admin.site.register(Contact)
admin.site.register(CodingProfile)


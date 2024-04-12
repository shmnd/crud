from django.contrib import admin
from students.models import Students

# Register your models here.
class studentsAdmin(admin.ModelAdmin):
    list_display=['sno','sname','sage','splace','smajor']
admin.site.register(Students,studentsAdmin)


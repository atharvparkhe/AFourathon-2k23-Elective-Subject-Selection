from django.contrib import admin
from .models import *


admin.site.register(StudentModel)
admin.site.register(TeacherModel)
admin.site.register(AdminModel)
admin.site.register(DepartmentModel)

# admin.site.register(FileModel)
from django.db import models
from base.models import *

class DepartmentModel(BaseModel):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class StudentModel(BaseUser):
    roll_no = models.CharField(max_length=50)
    department = models.ForeignKey(DepartmentModel, related_name="student_department", on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class TeacherModel(BaseUser):
    post = models.CharField(max_length=50)
    department = models.ForeignKey(DepartmentModel, related_name="department_teacher", on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class AdminModel(BaseUser):
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        self.is_staff = True
        super(AdminModel, self).save(*args, **kwargs) 


class FileModel(BaseModel):
    file = models.FileField(upload_to="upload", max_length=100)
    def __str__(self):
        return self.file

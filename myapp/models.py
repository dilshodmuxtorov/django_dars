from django.db import models
import datetime

class UserModel(models.Model):
    name = models.CharField(max_length=100, default="")
    age = models.IntegerField(default=0)
    email = models.EmailField()
    passport_number = models.CharField(max_length=9, unique=True)
    date_of_birth = models.DateTimeField(default=datetime.datetime.now())
    registrated_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = "users"
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Foydalanuvchilar"
        
    def __str__(self):
        return self.name


class CourseModel(models.Model):
    name = models.CharField(max_length=255, default="")
    # students = models.ManyToManyField(UserModel)

    class Meta:
        db_table = "course"
        verbose_name = "Kurs"
        verbose_name_plural = "Kurslar"
        
    def __str__(self):
        return self.name
    
class CourseStudentModel(models.Model):
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    course_id = models.ForeignKey(CourseModel, on_delete=models.SET_NULL,null=True)


    class Meta:
        db_table = "students_course"
        verbose_name = "Kursga yozilgan "
        verbose_name_plural = "Kursga Yozilganlar"
        
    def __str__(self):
        return str(self.user_id)
    

# CRUD - > 

# C ->  Create 
# R - > Retrieve 
# U -> update
# D -> delete o'chirib tashash
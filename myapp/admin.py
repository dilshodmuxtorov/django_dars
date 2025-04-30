from django.contrib import admin
from .models import UserModel, CourseModel, CourseStudentModel

class UserModelAdmin(admin.ModelAdmin):
    list_display = ['name','age','email','registrated_at','date_of_birth','id']
    search_fields = ['name','email']

class CourseStAdmin(admin.ModelAdmin):
    list_display = ['user_id','course_id']

admin.site.register(UserModel, UserModelAdmin)
admin.site.register(CourseModel)
admin.site.register(CourseStudentModel, CourseStAdmin)
from django.contrib import admin
from .models import Attendance,StudentExtra,LecturerExtra,Notice
# Register your models here. (by sumit.luv)
class StudentExtraAdmin(admin.ModelAdmin):
    pass
admin.site.register(StudentExtra, StudentExtraAdmin)

class LecturerExtraAdmin(admin.ModelAdmin):
    pass
admin.site.register(LecturerExtra, LecturerExtraAdmin)

class AttendanceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Attendance, AttendanceAdmin)

class NoticeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Notice, NoticeAdmin)

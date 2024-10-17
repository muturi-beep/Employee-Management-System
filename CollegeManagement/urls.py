"""
URL configuration for CollegeManagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from eMobilis import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name=''),

    path('adminclick', views.adminclick_view),
    path('lecturerclick', views.lecturerclick_view),
    path('studentclick', views.studentclick_view),


    path('adminsignup', views.admin_signup_view),
    path('studentsignup', views.student_signup_view,name='studentsignup'),
    path('lecturersignup', views.lecturer_signup_view),
    path('adminlogin', LoginView.as_view(template_name='adminlogin.html')),
    path('studentlogin', LoginView.as_view(template_name='studentlogin.html')),
    path('lecturerlogin', LoginView.as_view(template_name='lecturerlogin.html')),


    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='index.html'),name='logout'),


    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),


    path('admin-lecturer', views.admin_lecturer_view,name='admin-lecturer'),
    path('admin-add-lecturer', views.admin_add_lecturer_view,name='admin-add-lecturer'),
    path('admin-view-lecturer', views.admin_view_lecturer_view,name='admin-view-lecturer'),
    path('admin-approve-lecturer', views.admin_approve_lecturer_view,name='admin-approve-lecturer'),
    path('approve-lecturer/<int:pk>', views.approve_lecturer_view,name='approve-lecturer'),
    path('delete-lecturer/<int:pk>', views.delete_lecturer_view,name='delete-lecturer'),
    path('delete-lecturer-from-seMobilis/<int:pk>', views.delete_lecturer_from_eMobilis_view,name='delete-lecturer-from-school'),
    path('update-lecturer/<int:pk>', views.update_lecturer_view,name='update-lecturer'),
    path('admin-view-lecturer-salary', views.admin_view_lecturer_salary_view,name='admin-view-lecturer-salary'),


    path('admin-student', views.admin_student_view,name='admin-student'),
    path('admin-add-student', views.admin_add_student_view,name='admin-add-student'),
    path('admin-view-student', views.admin_view_student_view,name='admin-view-student'),
    path('delete-student-from-eMobilis/<int:pk>', views.delete_student_from_eMobilis_view,name='delete-student-from-school'),
    path('delete-student/<int:pk>', views.delete_student_view,name='delete-student'),
    path('update-student/<int:pk>', views.update_student_view,name='update-student'),
    path('admin-approve-student', views.admin_approve_student_view,name='admin-approve-student'),
    path('approve-student/<int:pk>', views.approve_student_view,name='approve-student'),
    path('admin-view-student-fee', views.admin_view_student_fee_view,name='admin-view-student-fee'),


    path('admin-attendance', views.admin_attendance_view,name='admin-attendance'),
    path('admin-take-attendance/<str:cl>', views.admin_take_attendance_view,name='admin-take-attendance'),
    path('admin-view-attendance/<str:cl>', views.admin_view_attendance_view,name='admin-view-attendance'),


    path('admin-fee', views.admin_fee_view,name='admin-fee'),
    path('admin-view-fee/<str:cl>', views.admin_view_fee_view,name='admin-view-fee'),

    path('admin-notice', views.admin_notice_view,name='admin-notice'),



    path('lecturer-dashboard', views.lecturer_dashboard_view,name='lecturer-dashboard'),
    path('lecturer-attendance', views.lecturer_attendance_view,name='lecturer-attendance'),
    path('lecturer-take-attendance/<str:cl>', views.lecturer_take_attendance_view,name='lecturer-take-attendance'),
    path('lecturer-view-attendance/<str:cl>', views.lecturer_view_attendance_view,name='lecturer-view-attendance'),
    path('lecturer-notice', views.lecturer_notice_view,name='lecturer-notice'),

    path('student-dashboard', views.student_dashboard_view,name='student-dashboard'),
    path('student-attendance', views.student_attendance_view,name='student-attendance'),




    path('aboutus', views.aboutus_view),
    path('contactus', views.contactus_view),
]

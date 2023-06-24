from django.urls import path
from . import views


urlpatterns = [
	# Main
	path('', views.homePage, name="index"),
	path('time-table/', views.timeTable, name="time-table"),
	path('contact-us/', views.contactPage, name="contact-us"),

	# Subjects
	path('add-subject/', views.addSubject, name="add-subject"),
	path('all-subjects/', views.allSubjects, name="all-subjects"),
	path('subject/<sub_id>/', views.singleSubject, name="single-subject"),
	path('admin-all-subjects/', views.adminAllSubjects, name="admin-all-subjects"),

	# Dashboard
	path('student-dashboard/', views.StudentDashboard, name="student-dashboard"),
	path('teacher-dashboard/', views.TeacherDashboard, name="teacher-dashboard"),
	path('admin-dashboard/', views.AdminDashboard, name="admin-dashboard"),
	path('api/graph-data/', views.get_graph_data, name="graph-data"),

	# Course Enrollment
	path('enroll/<num>/', views.enroll, name="enroll"),
	path('request-change-elective/<num>/', views.changeElective, name="change-elective"),
	
	# Teacher
	path('enrolled-students-list/', views.enrolledStudentList, name="enrolled-students-list"),
	path('student-profile/<stu_id>/', views.studentProfile, name="student-profile"),
	
]
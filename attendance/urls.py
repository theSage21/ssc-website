from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from attendance import views

urlpatterns = patterns(
	'',
	url(r'^$',views.home,name='attendance_home'),
	url(r'^(?P<studentid>\d+)/$',views.student_id,name='student_id'),
	url(r'^get_student$',views.get_student,name='get_student')
	
	
)

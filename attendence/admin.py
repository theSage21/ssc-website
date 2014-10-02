from django.contrib import admin
import attendence


class student_attendence_inline(admin.TabularInline):
	'''Inline addition for student_attendence'''
	model=attendence.models.student_attendence
	extra=20
	
class paper_attendence_admin(admin.ModelAdmin):
	'''Paper attendence admin'''
	
	inlines=[student_attendence_inline]
	list_display=['paper','date_from','date_to']
	list_filter=['date_from','date_to']
	search_fields=['paper']


admin.site.register(attendence.models.student_attendence)
admin.site.register(attendence.models.paper_attendence,paper_attendence_admin)

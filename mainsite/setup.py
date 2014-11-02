import os
import sys
import shutil
import random
import datetime
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stephens.settings")

from django.core.files import File

from django.contrib.auth.models import User,Group
from django.core.management import execute_from_command_line
from django.utils import timezone


def clean_to_string(string):
	'''
	removes non ascii characters
	'''
	allowed='ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'#alphabets
	allowed+=allowed.lower()#lowercase
	allowed+='!@#$%^&*()_+=-.,: '
	allowed+="'"
	allowed+='\n'
	new_str=''
	for i in string:
		if i in allowed:
			new_str+=i
	return new_str
import mainsite,attendance,office,events,admission,college_forms
function_list=[]
SETUP_SUPPORT_FOLDER='setup_support'




def homepage_slideshow(slideshow_pic_folder='homepage'):
	'''sets up the slideshow files in the homepage'''
	filepath=os.path.join(os.getcwd(),SETUP_SUPPORT_FOLDER,slideshow_pic_folder)
	files=os.listdir(filepath)
	for i in files:
		f=File(file(os.path.join(filepath,i)))
		a=mainsite.models.home_slideshow_photo()
		a.associated_photo=f
		a.name=i
		a.save()
function_list.append(homepage_slideshow)
#------------------------------------------------------------------------------------------------
def principal_desk_notices(principal_desk_folder='principal_desk'):
	'''sets up the principal desk notices'''
	filepath=os.path.join(os.getcwd(),SETUP_SUPPORT_FOLDER,principal_desk_folder)
	files=os.listdir(filepath)
	for i in files:
		f=file(os.path.join(filepath,i))
		a=mainsite.models.notification()
		a.title=i.split('.')[0].replace('_',' ')
		a.principal=True
		a.associated_file=File(f)
		content=f.readlines()
		a.description=' '.join(content[:3])[:100]
		a.save()
		f.close()
function_list.append(principal_desk_notices)
#------------------------------------------------------------------------------------------------
def notifications(folder='notifications'):
	'''sets up the notifications for the website'''
	filepath=os.path.join(os.getcwd(),SETUP_SUPPORT_FOLDER,folder)
	files=os.listdir(filepath)
	for i in files:
		a=mainsite.models.notification()
		a.title=i.split('.')[0].replace('_',' ')
		a.description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed quis odio vehicula, lobortis ante hendrerit, sodales dolor. Pellentesque quis massa in tellus vulputate pretium vel id ligula. Suspendisse potenti. Donec efficitur est odio, sit amet varius eros ornare in. </p>'
		f=file(os.path.join(filepath,i))
		a.associated_file=File(f)
		a.save()
		f.close()
function_list.append(notifications)
#------------------------------------------------------------------------------------------------
def run_function(fn):
	'''Runs the function and acts as a wrapper'''
	print fn.func_name.replace('_',' ').capitalize(),
	fn()
	print '--------->Done'
	
def run_setup():
	print '================================================================'
	for i in function_list:
		run_function(i)	
	print 'MAINSITE SETUP COMPLETE'
	print '================================================================'
	
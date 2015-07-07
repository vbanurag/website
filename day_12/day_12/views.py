from django.template import RequestContext
from django.shortcuts import render_to_response
from django.db import models
from day_12.models import lang
from day_12.models import stu
from day_12.models import writ

def home(request):
	ctx=RequestContext(request)
	temp_name="index.html"
	response= render_to_response(temp_name,{},ctx)
	return response

def aboutus(request):
	ctx=RequestContext(request)
	temp_name="about.html"
	response= render_to_response(temp_name,{},ctx)
	return response

def blog(request):
	ctx=RequestContext(request)
	temp_name="blog.html"
	response= render_to_response(temp_name,{},ctx)
	return response
def foer(request):
	ctx=RequestContext(request)
	temp_name="foer.html"
	values=lang.objects.all()
	stu_val=stu.objects.all()
	writer=writ.objects.all()
	print writer
	print stu_val
	print values
	response = render_to_response(temp_name,locals(),ctx)
	return response
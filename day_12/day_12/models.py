from django.db import models

class lang(models.Model):
	lang_name= models.CharField (max_length=20)
	score = models.IntegerField (max_length=2)

	def __unicode__(self):
		return self.lang_name

class stu(models.Model):
	stu_name =models.CharField(max_length=40)
	stu_course = models.CharField(max_length=40)
	stu_des=models.CharField(max_length=40)

	def __unicode__ (self):
		return self.stu_name

class writ(models.Model):
	langs=models.ForeignKey(lang)
	name= models.CharField(max_length=20)
	book=models.CharField(max_length=20)

	def __unicode__(self):
		return self.name

from django.contrib import admin
from django.db import models
from day_12.models import lang
from day_12.models import stu
from day_12.models import writ
admin.site.register(lang)
admin.site.register(writ)
admin.site.register(stu)
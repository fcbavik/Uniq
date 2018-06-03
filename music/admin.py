from django.contrib import admin
from .models import Subject, File, Forum, Question

admin.site.register(Subject)
admin.site.register(File)
admin.site.register(Forum)
admin.site.register(Question)

from django.contrib import admin
from .models import blog

@admin.register(blog)
class BlogRegister(admin.ModelAdmin):
    list_display=['id','user','name','datetime']
    

from django.contrib import admin
# from .models import Student
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ('name')
# admin.site.register(Student,StudentAdmin)
# # Register your models here.
from .models import Article,Category
# class ArticleAdmin(admin.ModelAdmin):
#     list_display = (Article.title)
admin.site.register(Article)
admin.site.register(Category)
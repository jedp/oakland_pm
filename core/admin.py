# from django.contrib import admin
# from .models import FAQ, QuestionAnswer, Category
# 
# class QuestionAnswerInline(admin.StackedInline):
#     model = QuestionAnswer
#     extra = 0
# 
# class CategoryAdmin(admin.ModelAdmin):
#     inlines = [QuestionAnswerInline]
#     fields = ['name']
#     save_on_top = True
#     
# class CategoryInline(admin.StackedInline):
#     model = Category
#     extra = 0
#     
# class FAQAdmin(SingletonAdmin):
#     inlines = [CategoryInline]
#     save_on_top = True
# 
# admin.site.register(FAQ, FAQAdmin)
# admin.site.register(Category, CategoryAdmin)
# 
# class PhoneField(models.CharField): pass
# class School(models.Model):
# class UserProfile(models.Model):
# class Contact(models.Model):
# class Category(models.Model):
# class Location(models.Model):
# class BusStop(models.Model):
# class BartStop(models.Model):
# class Address(models.Model):
# class Organization(models.Model):
# class EventDate(models.Model):
# class Program(models.Model):
# class Comment(models.Model):
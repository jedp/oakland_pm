from django.contrib import admin
from core.models import Profile,School,Address,GIS,EventDate,Contact,Category,SubCategory,Organization,Program,ProgramStatus,ProgramType,WatchList,WaitList,PublicTransport

# class QuestionAnswerInline(admin.StackedInline):
#     model = QuestionAnswer
#     extra = 0
# 

# class ProfileAdmin(admin.ModelAdmin):
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


class ProfileAdmin(admin.ModelAdmin):
    pass

class SchoolAdmin(admin.ModelAdmin):
    pass

class AddressAdmin(admin.ModelAdmin):
    pass

class GISAdmin(admin.ModelAdmin):
    pass

class EventDateAdmin(admin.ModelAdmin):
    pass

class ContactAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

class SubCategoryAdmin(admin.ModelAdmin):
    pass

class OrganizationAdmin(admin.ModelAdmin):
    pass

class ProgramAdmin(admin.ModelAdmin):
    pass

class ProgramStatusAdmin(admin.ModelAdmin):
    pass

class ProgramTypeAdmin(admin.ModelAdmin):
    pass

class WatchListAdmin(admin.ModelAdmin):
    pass

class WatchListAdmin(admin.ModelAdmin):
    pass

class PublicTransportAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, ProfileAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(GIS, GISAdmin)
admin.site.register(EventDate, EventDateAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(ProgramStatus, ProgramStatusAdmin)
admin.site.register(ProgramType, ProgramTypeAdmin)
admin.site.register(WatchList, WatchListAdmin)
admin.site.register(WaitList, WaitListAdmin)
admin.site.register(PublicTransport, PublicTransportAdmin)


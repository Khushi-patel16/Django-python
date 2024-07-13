from django.contrib import admin
#from blog.models import ContactModel, ServiceModel, AboutModel ,ClientModel
from blog.models import *

# Register your models here.
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('email',)
admin.site.register(Subscribe,SubscribeAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display=('name','email','subject','message')

admin.site.register(ContactModel,ContactAdmin)

class ServiceItemInline(admin.TabularInline):
    model = ServiceItem
    extra = 1  # Number of empty forms to display

class ServiceAdmin(admin.ModelAdmin):
    list_display=('icon', 'service','icon_desc')
    inlines = [ServiceItemInline]

admin.site.register(ServiceModel,ServiceAdmin)

class ListItemInline(admin.TabularInline):
    model = ListItem
    extra = 1  # Number of empty forms to display

class AboutAdmin(admin.ModelAdmin):
    list_display=('image','tagline', 'para1', 'para2')
    inlines = [ListItemInline]
admin.site.register(AboutModel, AboutAdmin)

class ClientAdmin(admin.ModelAdmin):
    list_display= ('title', 'image')
admin.site.register(ClientModel, ClientAdmin)

class CountsAdmin(admin.ModelAdmin):
    list_display=('icon','counter_end','title','description')
admin.site.register(Counts,CountsAdmin)

class TestimonialAdmin(admin.ModelAdmin):
    list_display=('image','name','post','description')
admin.site.register(Testimonials,TestimonialAdmin)

class TeamAdmin(admin.ModelAdmin):
    list_display=('image','name','post')
admin.site.register(Team,TeamAdmin)

class FeatureAdmin(admin.ModelAdmin):
    list_display=('icon', 'title','description')

admin.site.register(Features,FeatureAdmin)

class PortfolioAdmin(admin.ModelAdmin):
    list_display=('title','category','image')
admin.site.register(Portfolio,PortfolioAdmin)

# class PortDetAdmin(admin.ModelAdmin):
    # list_display=('title','category','client','project_date','project_url','description','images','tagline')
# admin.site.register(Portfolio_details,PortDetAdmin)


class PortfolioImageInline(admin.TabularInline):
    model = PortfolioImage
    extra = 1  # Number of empty forms to display

@admin.register(Portfolio_details)
class PortDetAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'client', 'project_date')
    search_fields = ('title', 'category', 'client')
    inlines = [PortfolioImageInline]

@admin.register(PortfolioImage)
class PortfolioImageAdmin(admin.ModelAdmin):
    pass


class HeaderAdmin(admin.ModelAdmin):
    list_display = ('site_name','line1','line2')
admin.site.register(Header,HeaderAdmin)    

class HeroAdmin(admin.ModelAdmin):
    list_display=('icon','title')
admin.site.register(Hero,HeroAdmin)

class FooterAdmin(admin.ModelAdmin):
    list_display = ('address','phone','email','newsletter')
admin.site.register(Footer,FooterAdmin)

class SocialAdmin(admin.ModelAdmin):
    list_display=('icon','link')
admin.site.register(Social,SocialAdmin)
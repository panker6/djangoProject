from django.contrib import admin
from products.models import Category, Page
from products.models import UserProfile


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
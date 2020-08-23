from django.contrib import admin

from blog.models import Category, Post, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'parent')
    prepopulated_fields = {'slug': ('name', )}


class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'name', 'created_date', 'update_date', 'product', 'category', 'to_display', 'for_auth')
    list_filter = ('product', 'created_date', 'category')
    list_editable = ('name', 'to_display', 'for_auth')
    prepopulated_fields = {'slug': ('name', )}


class ProductAdmin(admin.ModelAdmin):
    list_display = ('author', 'name', 'created_date', 'to_display', 'for_auth')
    list_filter = ('created_date', )
    list_editable = ('name', 'to_display', 'for_auth')
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Product, ProductAdmin)


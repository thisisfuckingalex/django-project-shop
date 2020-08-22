from django.contrib import admin

from user.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'id',]
    list_editable = ['first_name', 'last_name', 'id']
    list_filter = ['created_date']


admin.site.register(Profile, ProfileAdmin)



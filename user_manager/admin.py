from django.contrib import admin

from user_manager.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    search_fields = ['id', 'name', 'email']

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'phone')

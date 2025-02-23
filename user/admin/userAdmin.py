from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models.user import MyUser

class MyUserAdmin(UserAdmin):
    model = MyUser
    list_display = ('email', 'username', 'date_of_birth', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    readonly_fields = ('created_at', 'updated_at') 
    filter_horizontal = ('groups', 'user_permissions')  

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('full_name', 'username', 'date_of_birth', 'bio', 'avatar',  'cover')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'created_at', 'updated_at')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'full_name', 'username', 'date_of_birth', 
                'password1', 'password2', 'is_staff', 'is_active', 'is_superuser'
            ),
        }),
    )

    search_fields = ('email', 'username')
    ordering = ('email',)

admin.site.register(MyUser, MyUserAdmin)
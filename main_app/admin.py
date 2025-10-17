from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, CareerCast

# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, CareerCast

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_verified', 'date_joined')
    list_filter = ('is_verified', 'is_staff', 'is_superuser')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('-date_joined',)

    def delete_queryset(self, request, queryset):
        for user in queryset:
            # Explicitly delete related CareerCast entries
            CareerCast.objects.filter(user=user).delete()
        super().delete_queryset(request, queryset)


# Register CareerCast with the Django Admin
@admin.register(CareerCast)
class CareerCastAdmin(admin.ModelAdmin):
    list_display = ('user', 'job_title', 'created_at', 'resume_file', 'video_file')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('job_title', 'user__email')
    readonly_fields = ('created_at', 'updated_at')

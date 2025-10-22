# from django.contrib.auth.models import AbstractUser
# from django.db import models
# import uuid
# import os
# from django.conf import settings


# def resume_upload_path(instance, filename):
#     return f'resumes/user_{instance.user.id}/{filename}'

# def video_upload_path(instance, filename):
#     return f'videos/user_{instance.user.id}/{filename}'

# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True)
#     otp = models.CharField(max_length=6, blank=True, null=True)
#     otp_created_at = models.DateTimeField(null=True, blank=True)
#     is_verified = models.BooleanField(default=False)

#     def get_profile_initials(self):
#         if self.first_name and self.last_name:
#             return f"{self.first_name[0]}{self.last_name[0]}".upper()
#         elif self.first_name:
#             return self.first_name[0].upper()
#         else:
#             return self.username[0].upper()

#     groups = models.ManyToManyField(
#         'auth.Group',
#         related_name='customuser_set',  # This is the key fix for avoiding clashes
#         blank=True,
#         help_text='The groups this user belongs to.'
#     )
    
#     user_permissions = models.ManyToManyField(
#         'auth.Permission',
#         related_name='customuser_permissions',  # This is the key fix for avoiding clashes
#         blank=True,
#         help_text='Specific permissions for this user.'
#     )

# class CareerCast(models.Model):
#     # In your models.py for CareerCast
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
# # Link to CustomUser
#     job_title = models.CharField(max_length=255)
#     job_description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     teleprompter_text = models.TextField(null=True, blank=True) 
#     updated_at = models.DateTimeField(auto_now=True)
    
#     # Resume file
#     resume_file = models.FileField(upload_to='career_casts/resumes/', null=True, blank=True)
    
#     # Video file
#     video_file = models.FileField(upload_to='career_casts/videos/', null=True, blank=True)

#     def __str__(self):
#         return self.job_title

from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
import os
from django.conf import settings

def resume_upload_path(instance, filename):
    return f'resumes/user_{instance.user.id}/{filename}'

def video_upload_path(instance, filename):
    return f'videos/user_{instance.user.id}/{filename}'

class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    otp = models.CharField(max_length=6, blank=True, null=True)
    otp_created_at = models.DateTimeField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)

    def get_profile_initials(self):
        if self.first_name and self.last_name:
            return f"{self.first_name[0]}{self.last_name[0]}".upper()
        elif self.first_name:
            return self.first_name[0].upper()
        else:
            return self.username[0].upper()

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to.'
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',
        blank=True,
        help_text='Specific permissions for this user.'
    )

class CareerCast(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # ADD THIS LINE
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=255)
    job_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    teleprompter_text = models.TextField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    resume_file = models.FileField(upload_to=resume_upload_path, null=True, blank=True)
    video_file = models.FileField(upload_to=video_upload_path, null=True, blank=True)

    def __str__(self):
        return self.job_title

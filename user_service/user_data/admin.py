from django.contrib import admin
from user_data.models import Email,PhoneNumber,User
# Register your models here.
admin.site.register(User)
admin.site.register(Email)
admin.site.register(PhoneNumber)

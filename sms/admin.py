from django.contrib import admin
from sms.models import Recipients
# Register your models here.

class RecipientsAdminFunctionality(admin.ModelAdmin):
    class Meta:
        model = Recipients

admin.site.register(Recipients,RecipientsAdminFunctionality)
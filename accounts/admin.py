from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from accounts.models import Account


class AccountAdmin(UserAdmin):
	list_display = ('username', 'manager','is_manager', 'is_admin', 'date_joined', 'is_active','last_login') #any field can be added to display 
	search_fields = ('username',)
	readonly_fields = ('date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

admin.site.register(Account, AccountAdmin)
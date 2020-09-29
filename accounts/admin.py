from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from accounts.models import Account


class AccountAdmin(UserAdmin):
	list_display = ('username', 'date_joined', 'last_login', 'is_admin', 'manager','is_manager') #any field can be added to display 
	search_fields = ('username',)
	readonly_fields = ('date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

admin.site.register(Account, AccountAdmin)
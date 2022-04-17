from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from inventory.models import specialist_setup


class specialist_inline(admin.StackedInline):

	model= specialist_setup
	can_delete= False
	verbose_name = 'Specialist Setup'
	verbose_name_plural= "Specialist Setup"

class UserAdmin(BaseUserAdmin):
	inlines= (specialist_inline,)



admin.site.unregister(User)
admin.site.register(User, UserAdmin)
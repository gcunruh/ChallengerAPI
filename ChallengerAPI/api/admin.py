from django.contrib import admin
from .models import SecurityQuestion, Answer, User

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name']
    fields = ['username', 'email', 'first_name', 'last_name']


class SecurityQuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'question']

admin.site.register(User, UserAdmin)
admin.site.register(SecurityQuestion, SecurityQuestionAdmin)
admin.site.register(Answer)

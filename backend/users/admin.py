from django.contrib import admin

from users.models import User, Category, Income


admin.site.register(User)
admin.site.register(Category)
admin.site.register(Income)

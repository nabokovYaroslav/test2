from django.contrib import admin

from authentication.models import Income, Category
from costs.models import Cost


admin.site.register(Income)
admin.site.register(Category)
admin.site.register(Cost)
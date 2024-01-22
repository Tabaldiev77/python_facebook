from django.contrib import admin
from myapp.models import laptop


@admin.register(laptop)
class laptopAdmin(admin.ModelAdmin):
    list_display = ('title',)



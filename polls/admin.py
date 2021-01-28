from django.contrib import admin

from .models import Option, Day, Rating

# Register your models here.

class OptionInline(admin.TabularInline):
    model = Option
    extra = 1

class DayAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['date']}),
    ]
    inlines = [OptionInline]

admin.site.register(Option)
admin.site.register(Day, DayAdmin)
admin.site.register(Rating)

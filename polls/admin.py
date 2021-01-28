from django.contrib import admin

from .models import Option, Day, Serving, Rating

# Register your models here.

class ServingInline(admin.TabularInline):
    model = Serving
    extra = 1

class DayAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['date']}),
    ]
    inlines = [ServingInline]

admin.site.register(Option)
admin.site.register(Day, DayAdmin)
admin.site.register(Serving)
admin.site.register(Rating)

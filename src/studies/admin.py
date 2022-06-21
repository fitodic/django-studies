from django.contrib import admin

from .models import Trial


@admin.register(Trial)
class TrialAdmin(admin.ModelAdmin):
    list_display = ("name", "percent_enabled", "is_enabled")
    search_fields = ("name",)

    def has_add_permission(self, request):
        return False

from django.contrib import admin

from .models import Experiment


@admin.register(Experiment)
class ExperimentAdmin(admin.ModelAdmin):
    list_display = ("name", "percent_enabled", "is_enabled")
    search_fields = ("name",)

    def has_add_permission(self, request):  # pragma: no cover
        return False

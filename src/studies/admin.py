from django.contrib import admin

from .models import ExperimentConfig


@admin.register(ExperimentConfig)
class ExperimentConfigAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "percent_enabled",
        "is_enabled",
        "first_run",
        "last_run",
    )
    list_filter = (
        "first_run",
        "last_run",
    )
    search_fields = ("name",)

    def has_add_permission(self, request):  # pragma: no cover
        return False

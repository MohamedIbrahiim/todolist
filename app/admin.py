"""
Admin view which will represent admin actions and ui
"""
from django.db.models import Q, F, QuerySet
from django.utils import timezone
from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from .models import Todo


class TaskStatusFilter(SimpleListFilter):
    """
    Custom Filter which will filter Task Status by :
        OverDue, Finished, Pending (not done Yet)
    """

    title = "Task Status"
    parameter_name = "task_status"

    def lookups(self, request, model_admin):
        return [
            ("OverDue", "OverDue"),
            ("Finished", "Finished"),
            ("Pending", "Pending"),
        ]

    def queryset(self, request, queryset) -> QuerySet:
        if self.value() == "OverDue":
            return queryset.filter(
                Q(due_date__lt=timezone.now(), is_finished=False)
                | Q(finished_at__gt=F("due_date"))
            )
        if self.value() == "Finished":
            return queryset.filter(is_finished=True)
        if self.value() == "Pending":
            return queryset.filter(is_finished=False)
        return queryset


class ToDoAdmin(admin.ModelAdmin):
    """
    Class which will represent what to show and hide at ToDo model
    which will implement display list - list of filters -
    fields to be added to create todo task
    """

    list_display = ["description", "creator", "end_user", "is_finished"]
    list_filter = [TaskStatusFilter]
    fieldsets = ((None, {"fields": ("end_user", "description", "due_date")}),)

    def save_model(self, request, obj, form, change) -> None:
        obj.creator = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Todo, ToDoAdmin)

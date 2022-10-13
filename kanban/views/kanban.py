# from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from kanban.models import Team

# from kanban.api.serializers import KanbanFilterSerializer
# from kanban.forms import


@login_required
def check_user_access(request):
    id = request.user.pk
    check = Team.objects.filter(user_name=id)
    if not check:
        return False
    else:
        return True


@login_required
def manager(request):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        template_path = "kanban/pages/kanban_manager.html"

        return render(
            request,
            template_path,
        )

    except Exception as error:
        print("Internal error:", error)
        raise

from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from helpdesk.api.serializers import DemandFilterSerializer
from helpdesk.forms import DemandFormCreate, DemandFormUpdate
from helpdesk.models import Demand, Historic
from ti.models import Department, Profile


@login_required
def demand_view_list_by_user(request):
    try:
        id = request.user.pk
        # user_name = request.user.username
        # print("REQUEST::::", user_id, user_name)
        demands = Demand.objects.filter(user_name=id).exclude(status__name="Finalizado")
        # print("Demands:::", demands)

        context = {"demands": demands}
        template_path = "helpdesk/pages/demand_list_open.html"

        return render(
            request,
            template_path,
            context,
        )
    except Exception as error:
        print("Internal error:", error)
        raise


@login_required
def demand_view_list_done(request):
    try:
        id = request.user.pk
        demands = (
            Demand.objects.filter(user_name=id)
            .filter(status__name="Finalizado")
            .order_by("-id")
        )
        # print("Demands:::", demands)

        demand_filter = DemandFilterSerializer(request.GET, queryset=demands)

        context = {"demands": demands, "demand_filter": demand_filter}
        template_path = "helpdesk/pages/demand_list_done_filter.html"

        return render(
            request,
            template_path,
            context,
        )
    except Exception as error:
        print("Internal error:", error)
        raise


# envia form importado / None para enviar o mesmo vazio
# valida formulário para salvar
# redireciona para a rota da lista pelo apelido
# Request .post pega o formulário, files as medias
@login_required
def demand_view_create(request):
    try:
        user_id = request.user.pk
        print(user_id)

        department_id = (
            Profile.objects.filter(user=user_id)
            .values("department")[0]
            .get("department")
        )
        # department_id = profile_user.values("user")
        # department_id2 = profile_user.values_list("user")
        # department_id = profile_user.values("department")[0].get("department")
        # department_id2 = profile_user.values_list("department")

        # print("department_id:::", department_id)
        # print("department_id2:::", department_id2)

        form = DemandFormCreate(request.POST or None, request.FILES or None)
        form.fields["user_name"].initial = user_id
        # form.fields["user_name"].widget.attrs["disabled"] = True
        form.fields["user_name"].widget = forms.HiddenInput()
        form.fields["department"].initial = department_id
        form.fields["department"].widget = forms.HiddenInput()

        # form.fields["department"].widget.attrs["disabled"] = True

        # form.fields["department"].initial = department_id

        context = {"form": form}
        template_path = "helpdesk/pages/demand_create.html"

        if form.is_valid():
            form.save()
            return redirect("demands_list_by_user")

        return render(request, template_path, context)

    except Exception as error:
        print("Internal error:", error)
        raise


@login_required
def demand_view_details(request, id):
    try:
        # print("ID:::", id)
        demand = get_object_or_404(Demand, pk=id)
        # user_id = request.user.pk
        form = DemandFormUpdate(request.POST or None, instance=demand)
        form.fields["user_name"].widget.attrs["disabled"] = True
        form.fields["department"].widget.attrs["disabled"] = True
        form.fields["category"].widget.attrs["disabled"] = True
        form.fields["title"].widget.attrs["disabled"] = True
        form.fields["description"].widget.attrs["disabled"] = True
        form.fields["image"].widget.attrs["disabled"] = True
        form.fields["attendant"].widget.attrs["disabled"] = True
        form.fields["status"].widget.attrs["disabled"] = True
        form.fields["solution"].widget.attrs["disabled"] = True

        historic = Historic.objects.filter(demand_id=id)

        context = {"form": form, "historic": historic}
        template_path = "helpdesk/pages/demand_details.html"

        return render(request, template_path, context)

    except Exception as error:
        print("Internal error:", error)
        raise


@login_required
def demand_view_delete(request, id):
    try:
        demand = get_object_or_404(Demand, pk=id)
        context = {"demand": demand}
        template_path = "helpdesk/pages/demand_delete.html"

        if request.method == "POST":
            demand.delete()
            return redirect("demands_list_by_user")

        return render(request, template_path, context)
    except Exception as error:
        print("Internal error:", error)
        raise

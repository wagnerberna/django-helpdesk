import pandas as pd
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from helpdesk.models import Demand, Support
from kanban.models import Project, Task
from ti.service.check_user_access import check_user_access
from ti.service.dataframe import dataframe_desktop_ranking
from inventory.models import Inventory
from ti.models import Department


@login_required
def api_technicals_demand(request):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")
        
        techinical = Support.objects.all()
        techinical_ids = techinical.all().values("id")
        techinical_user_names_ids = techinical.all().values("user_name")

        # print(techinical_ids, techinical_user_names_ids)

        techinicals_labels = []
        demands_total_per_technical = []

        for techinical_id in techinical_ids:
            techinical_total_demmand = Demand.objects.filter(
            attendant__id=techinical_id.get("id")
            ).count()
            demands_total_per_technical.append(techinical_total_demmand)
        
        for techinical_user_name_id in techinical_user_names_ids:
            id_to_find = techinical_user_name_id.get("user_name")
            user_name = User.objects.filter(id = id_to_find).values("username")[0].get("username")
            techinicals_labels.append(user_name)
            
        # print(techinicals_labels)
        # print(demands_total_per_technical)

        context = {
            "data": demands_total_per_technical,
            "labels": techinicals_labels,
        }

        return JsonResponse(context)

    except Exception as error:
        print("Internal error:", error)
        raise


@login_required
def api_technicals_tasks(request):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        techinical_Wagner_id = (
            User.objects.filter(username="wagner.berna").values("id")[0].get("id")
        )
        techinical_leonardo_id = (
            User.objects.filter(username="leonardo.susin").values("id")[0].get("id")
        )

        # Gráfico Tarefas Projetos
        tasks_leonardo = Task.objects.filter(
            task_owner__user_name=techinical_leonardo_id
        ).count()
        tasks_wagner = Task.objects.filter(
            task_owner__user_name=techinical_Wagner_id
        ).count()

        techinicals_labels = ["Leonardo.susin", "Wagner.berna"]
        tasks_total_per_techinical = [tasks_leonardo, tasks_wagner]

        context = {"data": tasks_total_per_techinical, "labels": techinicals_labels}
        # print(context)

        return JsonResponse(context)

    except Exception as error:
        print("Internal error:", error)
        raise


@login_required
def api_project_tasks(request):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        # Table Projects
        projects_names = list(Project.objects.all().values_list("name"))

        projects_labels = []
        tasks_to_do = []
        tasks_doing = []
        tasks_blocked = []
        tasks_done = []
        tasks_active = []
        tasks_done = []
        tasks_total = []
        project_percentage = []
        label_status = ["TO DO", "DOING", "BLOCKED", "DONE"]

        for project in projects_names:
            tasks_total_count = Task.objects.filter(project__name=project[0]).count()
            if not tasks_total_count:
                tasks_total_count = 1

            tasks_to_do_count = Task.objects.filter(
                project__name=project[0], status__name="TO DO"
            ).count()

            tasks_doing_count = Task.objects.filter(
                project__name=project[0], status__name="DOING"
            ).count()

            tasks_blocked_count = Task.objects.filter(
                project__name=project[0], status__name="BLOCKED"
            ).count()

            tasks_done_count = Task.objects.filter(
                project__name=project[0], status__name="DONE"
            ).count()

            tasks_active_count = tasks_total_count - tasks_done_count

            percentage = round((tasks_done_count / tasks_total_count) * 100)

            if percentage != 100:
                projects_labels.append(project[0])
                tasks_total.append(tasks_total_count)
                tasks_active.append(tasks_active_count)
                tasks_to_do.append(tasks_to_do_count)
                tasks_doing.append(tasks_doing_count)
                tasks_blocked.append(tasks_blocked_count)
                tasks_done.append(tasks_done_count)
                project_percentage.append(percentage)

        context = {
            "labels": projects_labels,
            "label_status": label_status,
            "tasks_total": tasks_total,
            "tasks_active": tasks_active,
            "tasks_to_do": tasks_to_do,
            "tasks_doing": tasks_doing,
            "tasks_blocked": tasks_blocked,
            "tasks_done": tasks_done,
            "project_percentage": project_percentage,
        }

        return JsonResponse(context)

    except Exception as error:
        print("Internal error:", error)
        raise


@login_required
def api_workstations_ranking(request):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        ranking_a = Inventory.objects.filter(ranking__name="A").count()
        ranking_b = Inventory.objects.filter(ranking__name="B").count()
        ranking_c = Inventory.objects.filter(ranking__name="C").count()
        ranking_d = Inventory.objects.filter(ranking__name="D").count()
        ranking_e = Inventory.objects.filter(ranking__name="E").count()

        ranking_workstation = [ranking_a, ranking_b, ranking_c, ranking_d, ranking_e]
        ranking_labels = ["A-i7", "B-i5", "C-i3", "D-Core", "E-Celeron"]

        context = {
            "data": ranking_workstation,
            "labels": ranking_labels,
        }

        return JsonResponse(context)

    except Exception as error:
        print("Internal error:", error)
        raise


def api_workstations_department_ranking(request):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        departments = Department.objects.all().values("name")
        inventory = Inventory.objects.all()
        # print(departments)
        # print(inventory)

        ranking_labels = ["A", "B", "C", "D", "E"]
        departments_labels = []
        ranking_a = []
        ranking_b = []
        ranking_c = []
        ranking_d = []
        ranking_e = []

        # print(inventory.filter(department__name="TI", ranking__name="A").count())

        for department in departments:
            count_a = inventory.filter(
                department__name=department["name"], ranking__name="A"
            ).count()
            count_b = inventory.filter(
                department__name=department["name"], ranking__name="B"
            ).count()
            count_c = inventory.filter(
                department__name=department["name"], ranking__name="C"
            ).count()
            count_d = inventory.filter(
                department__name=department["name"], ranking__name="D"
            ).count()
            count_e = inventory.filter(
                department__name=department["name"], ranking__name="E"
            ).count()

            departments_labels.append(department["name"])
            ranking_a.append(count_a)
            ranking_b.append(count_b)
            ranking_c.append(count_c)
            ranking_d.append(count_d)
            ranking_e.append(count_e)

            print(count_a, count_b, count_c, count_d, count_e)
            # print(department["name"])

        # print(departments_labels)

        context = {
            "departments_labels": departments_labels,
            "ranking_labels": ranking_labels,
            "ranking_a": ranking_a,
            "ranking_b": ranking_b,
            "ranking_c": ranking_c,
            "ranking_d": ranking_d,
            "ranking_e": ranking_e,
        }

        return JsonResponse(context)

    except Exception as error:
        print("Internal error:", error)
        raise

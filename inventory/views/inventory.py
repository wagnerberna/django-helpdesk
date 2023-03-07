from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from inventory.models import (CpuDescription, CpuGeneration, CpuManufacturer,
                              CpuModel, HardDiskSize, Hardware, Inventory,
                              Invoice, MemorySize, OperationalSystem, Ranking,
                              Software, SystemArchitecture,
                              WorkstationManufacturer, WorkstationModel,
                              WorkstationType)


@login_required
def inventory_view_list_all(request):
    try:

    context = {"inventory": "inventory"}
    template_path = "inventory/pages/iventory_list_all.html"

        return render(
            request,
            template_path,
            context,
        )

    except Exception as error:
        print("Internal error:", error)
        raise
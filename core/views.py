from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Record
from .forms import AddRecordForm


def home(request):
    context = {}
    return render(request, "core/home.html", context)


@login_required
def add_record(request):
    form = AddRecordForm()

    if request.method == "POST":
        form = AddRecordForm(request.POST)

        if form.is_valid():
            form.save(commit=False)
            form.instance.created_by = request.user
            form.save()
            messages.success(request, "New Record Created Successfully")
            return redirect("core:dashboard")

    context = {
        "form": form,
        "title": "Create New Record",
    }

    return render(request, "core/add_record.html", context)


@login_required
def update_record(request, pk):
    record = get_object_or_404(Record, pk=pk, created_by=request.user)
    form = AddRecordForm(instance=record)
    if request.method == "POST":
        form = AddRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Updated Successfully")
            return redirect("core:dashboard")

    context = {
        "title": "Update Record",
        "form": form,
    }
    return render(request, "core/update_record.html", context)


@login_required
def dashboard(request):
    records = Record.objects.filter(created_by=request.user)

    context = {"records": records}
    return render(request, "core/dashboard.html", context)


@login_required
def delete_record(request, pk):
    records = get_object_or_404(Record, pk=pk, created_by=request.user)
    if request.method == "POST":
        records.delete()
        messages.success(request, "Record deleted successfully")
        return redirect("core:home")

    context = {"records": records,
               "title": "Delete"
               }

    return render(request, "core/delete_record.html", context)


def record_detail(request, pk):
    record = get_object_or_404(Record, pk=pk)

    context = {"record": record}
    return render(request, "core/record_detail.html", context)

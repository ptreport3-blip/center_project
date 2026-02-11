from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Appointment
from datetime import datetime, timedelta
import json
from django.contrib.auth.decorators import login_required


def dashboard_view(request):
    return render(request, "clinic/dashboard.html")


def calendar_view(request):
    return render(request, "clinic/calendar.html")


def appointments_list(request):
    data = []

    for app in Appointment.objects.all():
        start = datetime.combine(app.date, app.time)
        end = start + timedelta(minutes=15)

        data.append({
            "id": app.id,
            "title": app.patient.name,
            "start": start.isoformat(),
            "end": end.isoformat(),
        })

    return JsonResponse(data, safe=False)


@csrf_exempt
def add_appointment(request):
    if request.method == "POST":
        data = json.loads(request.body)
        start = datetime.fromisoformat(data["start"])

        Appointment.objects.create(
            patient_id=1,
            doctor_id=1,
            date=start.date(),
            time=start.time(),
        )

        return JsonResponse({"status": "created"})


@csrf_exempt
def delete_appointment(request, pk):
    Appointment.objects.filter(id=pk).delete()
    return JsonResponse({"status": "deleted"})
@login_required
def dashboard_view(request):
    return render(request, "clinic/dashboard.html")


@login_required
def calendar_view(request):
    return render(request, "clinic/calendar.html")
@login_required
def accounting_view(request):
    plans = TreatmentPlan.objects.all()
    return render(request, "clinic/accounting.html", {
        "plans": plans
    })

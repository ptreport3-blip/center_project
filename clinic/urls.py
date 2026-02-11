from django.urls import path
from . import views

urlpatterns = [
    path("calendar/", views.calendar_view, name="calendar"),
    path("", views.dashboard_view, name="dashboard"),   # 👈 الصفحة الرئيسية

    path("api/appointments/", views.appointments_list),
    path("api/appointments/add/", views.add_appointment),
    path("api/appointments/delete/<int:pk>/", views.delete_appointment),
    path("accounting/", views.accounting_view, name="accounting"),

]

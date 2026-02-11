from django.contrib import admin
from .models import Patient, Doctor, Appointment

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)
from django.contrib import admin
from .models import TreatmentPlan, Session

class SessionInline(admin.TabularInline):
    model = Session
    extra = 1

@admin.register(TreatmentPlan)
class TreatmentPlanAdmin(admin.ModelAdmin):
    list_display = (
        'patient',
        'total_sessions',
        'total_price',
        'paid_amount',
        'remaining_amount',
    )
    search_fields = ('patient__name',)
    inlines = [SessionInline]

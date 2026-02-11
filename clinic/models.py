from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.patient} - {self.date}"
class TreatmentPlan(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    total_sessions = models.PositiveIntegerField()
    price_per_session = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateField(auto_now_add=True)

    def total_price(self):
        return self.total_sessions * self.price_per_session

    def paid_amount(self):
        return sum(s.paid_amount for s in self.sessions.all())

    def remaining_amount(self):
        return self.total_price() - self.paid_amount()

    def __str__(self):
        return f"{self.patient.name} - Plan"
class Session(models.Model):
    plan = models.ForeignKey(
        TreatmentPlan,
        related_name="sessions",
        on_delete=models.CASCADE
    )
    date = models.DateField()
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.plan.patient.name} - {self.date}"

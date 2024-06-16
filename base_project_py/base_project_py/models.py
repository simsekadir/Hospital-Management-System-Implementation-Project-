from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
        ('admin', 'Admin'),
        ('pharmacist', 'Pharmacist'),
        ('receptionist', 'Receptionist'),
        ('lab_assistant', 'Lab Assistant'),
    )

    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='patient')

    def __str__(self):
        return self.username


class Appointment(models.Model):
    patient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='doctor_appointments')
    date = models.DateTimeField()
    reason = models.TextField()

    def __str__(self):
        return f"Appointment with {self.doctor} for {self.patient} on {self.date}"


class Medicine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField()
    expiry_date = models.DateField()

    def __str__(self):
        return self.name


class Prescription(models.Model):
    patient = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, related_name='prescriptions_patient')
    doctor = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, related_name='prescriptions_doctor')
    medicine = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True, editable=True)  # 'editable=True' eklenmiştir
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.patient} - {self.medicine} - {self.date}"

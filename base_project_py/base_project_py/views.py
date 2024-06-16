from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AppointmentForm, PrescriptionForm
from .models import Appointment, Prescription

def home(request):
    if request.user.is_authenticated:
        messages.success(request, f'Hoş geldiniz {request.user.username}!')
        is_admin = request.user.is_staff  # Admin kontrolü
    else:
        is_admin = False
    return render(request, 'home.html', {'is_admin': is_admin})

@login_required
def system_page(request):
    return render(request, 'system_page.html')

@login_required
def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointments.html', {'appointments': appointments})

@login_required
def appointment_create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Randevu başarıyla oluşturuldu.')
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'appointment_form.html', {'form': form})

@login_required
def prescription_list(request):
    prescriptions = Prescription.objects.all()
    return render(request, 'prescriptions.html', {'prescriptions': prescriptions})

@login_required
def prescription_create(request):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reçete başarıyla oluşturuldu.')
            return redirect('prescription_list')
    else:
        form = PrescriptionForm()
    return render(request, 'prescription_form.html', {'form': form})

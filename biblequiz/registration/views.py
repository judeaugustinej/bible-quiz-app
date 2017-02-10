from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from .models import Register
from .forms import RegisterForm


def home(request):
    return render(request, 'registration/home.html', {})


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.create_payment_time()
            student.select_group()
            student.save()
            return redirect('students')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

def students(request):
    students = Register.objects.all()
    return render(request, 'registration/students.html', {'students': students})


def student_detail(request, pk):
    student = get_object_or_404(Register, pk=pk)
    return render(request, 'registration/student_detail.html', {'student': student})
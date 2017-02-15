from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Register
from .forms import RegisterForm

@login_required
def home(request):
    return render(request, 'registration/home.html', {})

@login_required
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

@login_required
def students(request):
    group_a_students =  Register.objects.filter(group='A')
    group_b_students =  Register.objects.filter(group='B')
    group_c_students =  Register.objects.filter(group='C')
    group_d_students =  Register.objects.filter(group='D')
    return render(request, 'registration/students.html', {'group_a_students': group_a_students, 'group_b_students': group_b_students, 'group_c_students': group_c_students, 'group_d_students': group_d_students,})

@login_required
def student_detail(request, pk):
    student = get_object_or_404(Register, pk=pk)
    return render(request, 'registration/student_detail.html', {'student': student})


@login_required
def student_edit(request, pk):
    student = get_object_or_404(Register, pk=pk)
    if request.method == "POST":
        form = RegisterForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save(commit=False)
            student.select_group()
            student.save()
            return redirect('student_detail', pk=student.pk)
    else:
        form = RegisterForm(instance=student)
    return render(request, 'registration/register.html', {'form': form})

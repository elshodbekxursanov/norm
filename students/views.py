from django.shortcuts import render, redirect
from .form import StudentForm

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # list sahifaga o'tadi
    else:
        form = StudentForm()
        return render(request, 'student_create.html', {'form': form})

def student_list(request):
    from .models import Student
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


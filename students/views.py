from django.shortcuts import render, redirect
from .models import Student


def student_list(request):
    students = Student.objects.all().order_by('name')
    return render(request, 'student_list.html', {'students': students})   # ← 'students/' olib tashlandi


def student_create(request):
    if request.method == "POST":
        name   = request.POST.get('name', '').strip()
        age    = request.POST.get('age', '')
        email  = request.POST.get('email', '').strip()
        course = request.POST.get('course', '').strip()

        if not name or not age or not email or not course:
            return render(request, 'student_form.html', {
                'error': 'Barcha maydonlarni to‘ldiring!',
                'name': name,
                'age': age,
                'email': email,
                'course': course
            })

        try:
            age = int(age)
        except ValueError:
            return render(request, 'student_form.html', {
                'error': 'Yosh maydoniga faqat raqam kiriting!',
                'name': name,
                'age': age,
                'email': email,
                'course': course
            })

        Student.objects.create(
            name=name,
            age=age,
            email=email,
            course=course
        )
        return redirect('student_list')

    return render(request, 'student_form.html')
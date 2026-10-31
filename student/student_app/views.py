from django.shortcuts import render, redirect
from .models import Student, Course, Result


def students(request):
    data = Student.objects.all()
    return render(request, 'students.html', {'students': data})


def results(request):
    results = Result.objects.all()
    return render(request, 'results.html', {'results': results})

def add_student(request):
    courses = Course.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        roll = request.POST.get('roll')
        course_id = request.POST.get('course')   # safe

        if course_id:   # prevent empty submit
            Student.objects.create(
                name=name,
                roll_no=roll,
                course_id=course_id
            )
            return redirect('students')

    return render(request, 'add_student.html', {'courses': courses})

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse, HttpResponseBadRequest
from collections import Counter
from .models import Student
from .forms import StudentForm
from django.views.decorators.http import require_POST

# Create your views here.

from collections import Counter
from django.shortcuts import render
from .models import Student

def list_students(request):
    qs = Student.objects.filter(age__gte=18).order_by('name')
    course_counts = Counter(s.course for s in qs)
    for s in qs:
        s.highlight = course_counts[s.course] > 1
    return render(request, 'students_list.html', {'students': qs})


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student added successfully.')
            return redirect('students:list')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})

def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student updated successfully.')
            return redirect('students:list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_form.html', {'form': form, 'student': student})

@require_POST
def delete_student(request, pk):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        student = get_object_or_404(Student, pk=pk)
        student.delete()
        return JsonResponse({'success': True})
    return HttpResponseBadRequest('Invalid request')

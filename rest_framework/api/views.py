from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def students(request):
    students = {
        'name':'Nadil',
        'department':'bca',
        'year':'second',
        'place':'kozhikode'
    }
    return JsonResponse(students)

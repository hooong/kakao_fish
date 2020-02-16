from django.shortcuts import render

def start_btn(request):
    return render(request, 'start_btn.html')

def get_number(request):
    return render(request, 'show_number.html')
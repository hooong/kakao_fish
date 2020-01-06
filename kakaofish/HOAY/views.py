from django.shortcuts import render

def hoaymain(request):
    return render(request, "hoyamain.html")

def result(request):

    context = {}
    return render(request, "result.html", context)
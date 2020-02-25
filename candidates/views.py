from django.shortcuts import render

# Create your views here.
def candidate_(request):
    return render(request, 'candidates/candidate_.html')
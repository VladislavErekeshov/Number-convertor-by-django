from django.shortcuts import render, redirect
from .models import Convertor
from .forms import ConvertorForm

def index(request):
    error = ''
    if request.method == 'POST':
        convertor = ConvertorForm(request.POST)
        if convertor.is_valid():
            convertor.save()
            return redirect('ans')   
        else:
            error = 'Некорректная форма'
    convertor = ConvertorForm()
    context = {
        'convertor': convertor,
        'error': error,
    }
    return render(request, "main/index.html", context)

def ans(request):
    answer = Convertor.objects.order_by("-id")[:1]
    return render(request, "main/ans.html", {"answer": answer})

# Create your views here.

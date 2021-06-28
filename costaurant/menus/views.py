from django.shortcuts import render
from datetime import datetime


# Create your views here.
def index(request):
    today = datetime.now().date()
    context = {'today': today}
    return render(request, 'menus/index.html', context)

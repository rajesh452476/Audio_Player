from django.shortcuts import render
from django.http import HttpResponse

from travell.models import Song

# Create your views here.
def home(request):
    song = Song().__class__.objects.all()
    return render(request,'home.html',{'song':song})
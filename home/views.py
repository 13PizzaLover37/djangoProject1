from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse
from .models import Person
# Create your views here.

class Hello(View):
    def get(self, request):
        HttpResponse("Hi")

def Hi(self, request):
    HttpResponse("Hi")


class watch(View):
    def get(self, request):
        search_query = request.GET.get("search", "")
        people = Person.objects.all()
        if search_query:
            person = Person.objects.filter(name__icontains = search_query)
            return render(request, "home/home.html", {"people_list": person})
        else:
            return render(request, "home/home.html", {"people_list": people})

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ToDoList
from .forms import CreateNewList

def create(response):
    if response.method == 'POST':
        form = CreateNewList(response.POST)

        if form.is_valid():
            n=form.cleaned_data['name']
            t=ToDoList(name=n)
            t.save()

        return HttpResponseRedirect('/%i' %t.id)
    else:
        form = CreateNewList()
    return render(response, 'main.html', {'form': form})
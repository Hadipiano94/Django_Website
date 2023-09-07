from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item, TelBook
from .forms import CreateNewTel


def home(response):
    my_dict = {}
    return render(response, "main/home.html", my_dict)


def tdlist(response):
    tdos = ToDoList.objects
    my_dict = {
        "tdos_all": tdos.all(),
    }
    return render(response, "main/list.html", my_dict)


def create(response):
    if response.method == "POST":
        form = CreateNewTel(response.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            tel = form.cleaned_data["tel"]
            dnt_call = form.cleaned_data["dnt_call"]
            new_tel = TelBook(name=name, tel=tel, dnt_call=dnt_call)
            new_tel.save()
            return HttpResponseRedirect(f"/<{name}>")
    else:
        form = CreateNewTel()

    my_dict = {
        "form": form
    }
    return render(response, "main/create.html", my_dict)


def show_tels(response, name=None):
    tels_list = TelBook.objects.all()
    last_tel = name[1:-1]
    my_dict = {
        "tels_list": tels_list,
        "last_tel": last_tel,
    }
    return render(response, "main/show_tels.html", my_dict)

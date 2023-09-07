from django.db import models


class ToDoList(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=256)
    complete = models.BooleanField()

    def __str__(self):
        return self.text


class TelBook(models.Model):
    name = models.CharField(max_length=128)
    tel = models.CharField(max_length=64)
    dnt_call = models.BooleanField()

    def __str__(self):
        return self.name

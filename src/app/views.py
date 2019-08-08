from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import ExpenseModel
from django.urls import reverse_lazy

# Create your views here.


class ExpenseList(ListView):
    template_name = 'list.html'
    model = ExpenseModel


class ExpenseCreate(CreateView):
    template_name = 'create.html'
    model = ExpenseModel
    fields = ('name', 'datetime', 'genre', 'amount', 'is_outgo', 'memo')
    success_url = reverse_lazy('list')


class ExpenseUpdate(UpdateView):
    template_name = 'update.html'
    model = ExpenseModel
    fields = ('name', 'datetime', 'genre', 'amount', 'is_outgo', 'memo')
    success_url = reverse_lazy('list')


class ExpenseDelete(DeleteView):
    template_name = 'delete.html'
    model = ExpenseModel
    success_url = reverse_lazy('list')


class ExpenseDetail(DetailView):
    template_name = 'detail.html'
    model = ExpenseModel

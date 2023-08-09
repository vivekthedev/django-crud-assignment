from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import Contact

class HomeView(ListView):
    model = Contact
    success_url = "/"
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return self.model.objects.filter(name__icontains=query)
        return self.model.objects.all()
    

class ContactCreate(CreateView):
    model = Contact
    success_url = "/"
    fields = ['name', 'number', 'email', 'address']

class ContactDelete(DeleteView):
    model = Contact
    success_url = "/"

class ContactUpdate(UpdateView):
    model = Contact
    template_name_suffix = '_update'
    fields = ['name', 'number', 'email', 'address']
    success_url = "/"

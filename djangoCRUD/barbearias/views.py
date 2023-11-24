from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Barbearia

class BarbeariaListView(ListView):
    model = Barbearia

class BarbeariaCreateView(CreateView):
    model = Barbearia
    fields = ["nome", "endereco", "funcionarios"]
    success_url = reverse_lazy("barbearia_list")

class BarbeariaUpdateView(UpdateView):
    model = Barbearia
    fields = ["nome", "endereco", "funcionarios"]
    success_url = reverse_lazy("barbearia_list")

class BarbeariaDeleteView(DeleteView):
    model = Barbearia
    success_url = reverse_lazy("barbearia_list")
from django.shortcuts import render
from django.views import generic
from .models import Output, Program


class OutputList(generic.ListView):
    template_name = "output/output_list.html"
    model = Output
    context_object_name = "outputs"


class OutputDetail(generic.DetailView):
    template_name = "output/output_detail.html"
    model = Output
    context_object_name = "output"


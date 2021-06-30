from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import Output, Program
from .forms import OutputForm, ProgramForm

class OutputList(generic.ListView):
    template_name = "output/output_list.html"
    model = Output
    context_object_name = "outputs"


class OutputDetail(generic.DetailView):
    template_name = "output/output_detail.html"
    model = Output
    context_object_name = "output"


class OutputCreate(generic.CreateView):
    template_name = "output/output_create.html"
    model = Output
    form_class = OutputForm
    success_url = reverse_lazy("output:output_list")


# Program Model
def code_list(requests, output_id):
    """
    check output code
    :param output_id: output id
    :param requests:
    :return: html and params
    """
    codes: set = Program.objects.filter(output=output_id)

    params: dict = {
        "codes": codes,
        "output_id": output_id
    }
    return render(requests, 'output/code_list.html', params)


class CodeDetail(generic.DetailView):
    template_name = "output/code_detail.html"
    model = Program
    context_object_name = "code"






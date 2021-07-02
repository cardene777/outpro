from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic

from .models import Output, Program, Good
from .forms import OutputForm, ProgramForm


class OutputList(generic.ListView):
    template_name = "output/output_list.html"
    model = Output
    context_object_name = "outputs"


class OutputDetail(generic.DetailView):
    template_name = "output/output_detail.html"
    model = Output
    context_object_name = "output"

    def get_context_data(self, **kwargs):
        context = super(OutputDetail, self).get_context_data()
        context["program_count"] = Program.objects.filter(output=self.kwargs["pk"]).count()
        return context


class OutputCreate(generic.CreateView):
    template_name = "output/output_create.html"
    model = Output
    form_class = OutputForm
    success_url = reverse_lazy("output:output_list")


class OutputUpdate(generic.UpdateView):
    template_name = "output/output_update.html"
    model = Output
    form_class = OutputForm

    def get_success_url(self):
        return reverse('output:output_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(OutputUpdate, self).get_context_data()
        context["output_id"] = str(self.kwargs["pk"])
        return context


class OutputDelete(generic.DeleteView):
    template_name = "output/output_delete.html"
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
    codes: set = Program.objects.filter(output=output_id).order_by("good").reverse()

    params: dict = {
        "codes": codes,
        "output_id": output_id
    }
    return render(requests, 'output/code_list.html', params)


class CodeDetail(generic.DetailView):
    template_name = "output/code_detail.html"
    model = Program
    context_object_name = "code"

    def get_context_data(self, **kwargs):
        context = super(CodeDetail, self).get_context_data()
        context["good"] = str(Program.objects.get(id=str(self.kwargs["pk"])).good_count)
        return context


class CodeCreate(generic.CreateView):
    template_name = "output/code_create.html"
    model = Program
    form_class = ProgramForm

    def get_success_url(self):
        return reverse('output:output_detail', kwargs={'pk': self.object.output_id})

    def get_context_data(self, **kwargs):
        context = super(CodeCreate, self).get_context_data()
        context["output_id"] = self.kwargs["output_id"]
        return context


class CodeUpdate(generic.UpdateView):
    template_name = "output/code_update.html"
    model = Program
    form_class = ProgramForm

    def get_success_url(self):
        return reverse('output:code_detail', kwargs={'pk': int(self.object.pk)})

    def get_context_data(self, **kwargs):
        context = super(CodeUpdate, self).get_context_data()
        context["output_id"] = str(self.kwargs["output_id"])
        context["good"] = self.kwargs["good"]
        context["pks"] = self.kwargs["pk"]
        return context


class CodeDelete(generic.DeleteView):
    template_name = "output/code_delete.html"
    model = Program
    form_class = ProgramForm

    def get_success_url(self):
        return reverse('output:code_list', kwargs={'output_id': int(self.object.output_id)})


def good(requests):
    if requests.method == "POST":
        username: str = requests.POST["username"]
        program_id: int = int(requests.POST["program_id"])
        code = Program.objects.get(id=program_id)
        good_plus = int(Good.objects.filter(program=str(program_id)).count())

        # いいねを増やしつつ、Goodモデルに登録
        if Good.objects.filter(program=program_id, username=username).count() == 0:
            good_plus = int(Program.objects.get(id=str(program_id)).good_count) + 1
            data = Program.objects.get(id=str(program_id))
            data.good_count = good_plus
            data.save()

            data = Good(program=data, username=username)
            data.save()

        params: dict = {
            "pk": program_id,
            "good": good_plus,
            "code": code
        }
        return render(requests, 'output/code_detail.html', params)



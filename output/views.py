from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.db.models import Q

from .models import Output, Program, Good, ReviewCode, Message, Comment
from .forms import OutputForm, ProgramForm

import logging
logger = logging.getLogger(__name__)


def required_dict(username):
    required: dict = {
        "review_count": str(Program.objects.filter(review=True).count()),
        "review_code_count": str(ReviewCode.objects.filter(check=False).count()),
        "messages_count": str(Message.objects.filter(username=username).exclude(check=True).count())
    }
    return required


class OutputList(generic.ListView):
    template_name = "output/output_list.html"
    model = Output
    context_object_name = "outputs"

    def get_queryset(self):
        outputs = Output.objects.all()
        if 'word' in self.request.GET and self.request.GET['word'] is not None:
            word: str = self.request.GET['word']
            outputs = outputs.filter(Q(title__icontains=word) | Q(about__icontains=word) | Q(language__icontains=word))
        return outputs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(OutputList, self).get_context_data()
        username = ""
        if self.request.user.is_authenticated:
            username = self.request.user.username
        required: dict = required_dict(username)
        context["review_count"] = required["review_count"]
        context["review_code_count"] = required["review_code_count"]
        context["messages_count"] = required["messages_count"]
        return context


class OutputDetail(generic.DetailView):
    template_name = "output/output_detail.html"
    model = Output
    context_object_name = "output"

    def get_context_data(self, **kwargs):
        context = super(OutputDetail, self).get_context_data()
        context["program_count"] = Program.objects.filter(output=self.kwargs["pk"]).count()
        username = ""
        if self.request.user.is_authenticated:
            username = self.request.user.username
        required: dict = required_dict(username)
        context["review_count"] = required["review_count"]
        context["review_code_count"] = required["review_code_count"]
        context["messages_count"] = required["messages_count"]

        context["comments"] = Comment.objects.filter(output_id=self.kwargs["pk"]).order_by("created_at")
        return context


class OutputCreate(generic.CreateView):
    template_name = "output/output_create.html"
    model = Output
    form_class = OutputForm
    success_url = reverse_lazy("output:output_list")

    def get_context_data(self, **kwargs):
        context = super(OutputCreate, self).get_context_data()
        username = ""
        if self.request.user.is_authenticated:
            username = self.request.user.username
        required: dict = required_dict(username)
        context["review_count"] = required["review_count"]
        context["review_code_count"] = required["review_code_count"]
        context["messages_count"] = required["messages_count"]
        return context


class OutputUpdate(generic.UpdateView):
    template_name = "output/output_update.html"
    model = Output
    form_class = OutputForm

    def get_success_url(self):
        return reverse('output:output_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(OutputUpdate, self).get_context_data()
        context["output_id"] = str(self.kwargs["pk"])
        username = ""
        if self.request.user.is_authenticated:
            username = self.request.user.username
        required: dict = required_dict(username)
        context["review_count"] = required["review_count"]
        context["review_code_count"] = required["review_code_count"]
        context["messages_count"] = required["messages_count"]
        return context


class OutputDelete(generic.DeleteView):
    template_name = "output/output_delete.html"
    model = Output
    form_class = OutputForm
    success_url = reverse_lazy("output:output_list")

    def get_context_data(self, **kwargs):
        context = super(OutputDelete, self).get_context_data()
        username = ""
        if self.request.user.is_authenticated:
            username = self.request.user.username
        required: dict = required_dict(username)
        context["review_count"] = required["review_count"]
        context["review_code_count"] = required["review_code_count"]
        context["messages_count"] = required["messages_count"]
        return context


# Program Model
def code_list(requests, output_id):
    """
    check output code
    :param output_id: output id
    :param requests:
    :return: html and params
    """
    codes: set = Program.objects.filter(output=output_id).order_by("good").reverse()

    if 'word' in requests.GET and requests.GET['word'] is not None:
        word: str = requests.GET['word']
        codes: set = codes.filter(Q(name__icontains=word) | Q(description__icontains=word))

    params: dict = {
        "codes": codes,
        "output_id": output_id,
        "code_list": True,
    }
    username = ""
    if requests.user.is_authenticated:
        username = requests.user.username

    required: dict = required_dict(username)
    params.update(required)
    return render(requests, 'output/code_list.html', params)


class CodeDetail(generic.DetailView):
    template_name = "output/code_detail.html"
    model = Program
    context_object_name = "code"

    def get_context_data(self, **kwargs):
        context = super(CodeDetail, self).get_context_data()
        context["good"] = str(Program.objects.get(id=str(self.kwargs["pk"])).good_count)
        username = ""
        if self.request.user.is_authenticated:
            username = self.request.user.username
        required: dict = required_dict(username)
        context["review_count"] = required["review_count"]
        context["review_code_count"] = required["review_code_count"]
        context["messages_count"] = required["messages_count"]

        context["comments"] = Comment.objects.filter(program_id=self.kwargs["pk"]).order_by("created_at")
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
        username = ""
        if self.request.user.is_authenticated:
            username = self.request.user.username
        required: dict = required_dict(username)
        context["review_count"] = required["review_count"]
        context["review_code_count"] = required["review_code_count"]
        context["messages_count"] = required["messages_count"]
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
        username = ""
        if self.request.user.is_authenticated:
            username = self.request.user.username
        required: dict = required_dict(username)
        context["review_count"] = required["review_count"]
        context["review_code_count"] = required["review_code_count"]
        context["messages_count"] = required["messages_count"]
        return context


class CodeDelete(generic.DeleteView):
    template_name = "output/code_delete.html"
    model = Program
    form_class = ProgramForm

    def get_success_url(self):
        return reverse('output:code_list', kwargs={'output_id': int(self.object.output_id)})

    def get_context_data(self, **kwargs):
        context = super(CodeDelete, self).get_context_data()
        username = ""
        if self.request.user.is_authenticated:
            username = self.request.user.username
        required: dict = required_dict(username)
        context["review_count"] = required["review_count"]
        context["review_code_count"] = required["review_code_count"]
        context["messages_count"] = required["messages_count"]
        return context


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
            "code": code,
        }
        username = ""
        if requests.user.is_authenticated:
            username = requests.user.username

        required: dict = required_dict(username)
        params.update(required)
        return render(requests, 'output/code_detail.html', params)


class Review(generic.ListView):
    template_name = "output/review_list.html"
    model = Program

    def get_context_data(self, **kwargs):
        context = super(Review, self).get_context_data()
        context["codes"] = Program.objects.filter(review=True)
        username = ""
        if self.request.user.is_authenticated:
            username = self.request.user.username
        required: dict = required_dict(username)
        context["review_count"] = required["review_count"]
        context["review_code_count"] = required["review_code_count"]
        context["messages_count"] = required["messages_count"]
        return context


def review_on(requests, program_id):
    code: set = Program.objects.get(id=program_id)
    code.review = True
    code.save()

    good_count: str = str(code.good_count)

    params: dict = {
        "code": code,
        "good": good_count,
        "pk": int(program_id),
    }

    username = ""
    if requests.user.is_authenticated:
        username = requests.user.username

    required: dict = required_dict(username)
    params.update(required)
    return render(requests, 'output/code_detail.html', params)


def code_review(requests, program_id):
    if requests.method == "POST":
        program: set = Program.objects.get(id=requests.POST["program_id"])
        data = ReviewCode(program_id=program, username=requests.POST["username"],
                          review_code=requests.POST["code"])
        data.save()

        codes = Program.objects.filter(review=True)

        params: dict = {
            "message": "done",
            "codes": codes,
        }
        username = ""
        if requests.user.is_authenticated:
            username = requests.user.username

        required: dict = required_dict(username)
        params.update(required)
        return render(requests, 'output/review_list.html', params)

    code: str = Program.objects.get(id=program_id).code

    params: dict = {
        "code": code,
        "program_id": program_id,
    }

    username = ""
    if requests.user.is_authenticated:
        username = requests.user.username

    required: dict = required_dict(username)
    params.update(required)
    return render(requests, 'output/code_review.html', params)


def review_check(requests, review_id):
    review: set = ReviewCode.objects.get(id=review_id)

    params: dict = {
        "review": review,
        "review_id": review_id,
    }

    username = ""
    if requests.user.is_authenticated:
        username = requests.user.username

    required: dict = required_dict(username)
    params.update(required)

    return render(requests, 'output/review_check.html', params)


def review_message(requests):
    if requests.method == "POST":
        username: str = requests.POST["username"]
        review: set = ReviewCode.objects.get(id=requests.POST["review_id"])
        data = Message(review=review, username=requests.POST["review_username"], message=requests.POST["message"])
        data.save()

        review.check = True
        review.save()

        outputs: list = Output.objects.filter(username=username)
        programs: list = Program.objects.filter(username=username)

        review_codes: set = ReviewCode.objects.filter(check=False)

        params: dict = {
            "username": username,
            "outputs": outputs,
            "programs": programs,
            "review_codes": review_codes,
            "message": "done"
        }

        username = ""
        if requests.user.is_authenticated:
            username = requests.user.username

        required: dict = required_dict(username)
        params.update(required)

        return render(requests, 'accounts/profile.html', params)


def check_message(requests, username):
    messages: set = Message.objects.filter(username=username)

    params: dict = {
        "messages": messages,
    }

    username = ""
    if requests.user.is_authenticated:
        username = requests.user.username

    required: dict = required_dict(username)
    params.update(required)

    return render(requests, 'output/check_message.html', params)


def check_message_done(requests, message_id):
    message: set = Message.objects.get(id=message_id)
    message.check = True
    message.save()

    username = ""
    if requests.user.is_authenticated:
        username = requests.user.username

    messages: set = Message.objects.filter(username=username)

    params: dict = {
        "messages": messages,
    }

    required: dict = required_dict(username)
    params.update(required)

    return render(requests, 'output/check_message.html', params)


def comment(requests):
    if requests.method == "POST":
        comment_text: str = requests.POST["comment"]
        username = ""
        if requests.user.is_authenticated:
            username = requests.user.username

        output_id: str = requests.POST["output_id"]

        if requests.POST["message"] == "output":

            output = Output.objects.get(id=output_id)
            comment_data = Comment(output_id=output, program_id=None, username=requests.POST["username"], comment=comment_text)
            comment_data.save()

            program_count = Program.objects.filter(output=output_id).count()
            comments = Comment.objects.filter(output_id=output_id).order_by("created_at")

            params: dict = {
                "program_count": program_count,
                "comments": comments,
                "pk": int(output_id),
                "output": output
            }

            required: dict = required_dict(username)
            params.update(required)

            return render(requests, 'output/output_detail.html', params)
        else:
            code_id: str = requests.POST["code_id"]

            code = Program.objects.get(id=code_id)
            comment_data = Comment(output_id=None, program_id=code, username=requests.POST["username"], comment=comment_text)
            comment_data.save()

            comments = Comment.objects.filter(program_id=code_id).order_by("created_at")

            good = str(Program.objects.get(id=code_id).good_count)

            params: dict = {
                "comments": comments,
                "pk": int(code_id),
                "code": code,
                "good": good
            }

            required: dict = required_dict(username)
            params.update(required)

            return render(requests, 'output/code_detail.html', params)


import sys

from django import forms
from .models import Output, Program
from cloudinary.forms import CloudinaryFileField

sys.path.append('../')
from config import settings


class OutputForm(forms.ModelForm):
    class Meta:
        model = Output
        fields = ("username", "title", "about", "description", "image", "language")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['id'] = 'title'
        self.fields['title'].widget.attrs['name'] = 'title'
        self.fields['title'].widget.attrs['placeholder'] = 'タイトル（必須）'

        self.fields['about'].widget.attrs['class'] = 'form-control'
        self.fields['about'].widget.attrs['id'] = 'about'
        self.fields['about'].widget.attrs['name'] = 'about'
        self.fields['about'].widget.attrs['placeholder'] = '概要（必須）'

        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['id'] = 'description'
        self.fields['description'].widget.attrs['name'] = 'description'
        self.fields['description'].widget.attrs['placeholder'] = 'ルールなどの説明（必須）'

        self.fields['image'].widget.attrs['class'] = 'image form-control'
        self.fields['image'].widget.attrs['id'] = 'image'
        self.fields['image'].widget.attrs['name'] = 'image'

        self.fields['language'].widget.attrs['class'] = 'form-select form-select-lg mb-3'
        self.fields['language'].widget.attrs['id'] = 'language'
        self.fields['language'].widget.attrs['name'] = 'language'


class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ("username", "output", "name", "description", "code",
                  "image01", "image02", "image03", "image04", "good_count")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['output'].widget.attrs['class'] = 'form-control'
        self.fields['output'].widget.attrs['id'] = 'output'
        self.fields['output'].widget.attrs['name'] = 'output'

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['id'] = 'name'
        self.fields['name'].widget.attrs['name'] = 'name'
        self.fields['name'].widget.attrs['placeholder'] = '作品タイトル（必須）'

        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['id'] = 'description'
        self.fields['description'].widget.attrs['name'] = 'description'
        self.fields['description'].widget.attrs['placeholder'] = '作成したコードの説明（必須）'

        self.fields['code'].widget.attrs['class'] = 'form-control'
        self.fields['code'].widget.attrs['id'] = 'code'
        self.fields['code'].widget.attrs['name'] = 'code'
        self.fields['code'].widget.attrs['placeholder'] = 'コード（マークダウン形式）（必須）'

        self.fields['image01'].widget.attrs['class'] = 'image'
        self.fields['image01'].widget.attrs['id'] = 'image01'
        self.fields['image01'].widget.attrs['name'] = 'image01'

        self.fields['image02'].widget.attrs['class'] = 'image'
        self.fields['image02'].widget.attrs['id'] = 'image02'
        self.fields['image02'].widget.attrs['name'] = 'image02'

        self.fields['image03'].widget.attrs['class'] = 'image'
        self.fields['image03'].widget.attrs['id'] = 'image03'
        self.fields['image03'].widget.attrs['name'] = 'image03'

        self.fields['image04'].widget.attrs['class'] = 'image'
        self.fields['image04'].widget.attrs['id'] = 'image04'
        self.fields['image04'].widget.attrs['name'] = 'image04'

        self.fields['good_count'].widget.attrs['class'] = 'form-control'
        self.fields['good_count'].widget.attrs['id'] = 'good_count'
        self.fields['good_count'].widget.attrs['name'] = 'good_count'

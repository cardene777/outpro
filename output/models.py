from django.db import models
from mdeditor.fields import MDTextField


class Output(models.Model):
    class Meta:
        verbose_name = "アウトプット"
        verbose_name_plural = "アウトプット"

    title = models.CharField(
        verbose_name="アウトプットタイトル",
        max_length=150,
        blank=False,
        unique=True
    )

    about = models.TextField(
        verbose_name="概要",
        blank=False,
        unique=True
    )

    description = models.TextField(
        verbose_name="説明",
        blank=False,
        unique=True
    )

    image = models.ImageField(
        verbose_name="画像",
        blank=True,
        upload_to="images/",
        default="images/default.jpg"
    )

    def __str__(self):
        return str(self.title)


class Program(models.Model):
    class Meta:
        verbose_name = "プログラム"
        verbose_name_plural = "プログラム"

    output = models.ForeignKey(
        Output,
        verbose_name="アウトプット",
        on_delete=models.CASCADE
    )

    name = models.CharField(
        verbose_name="プログラム名",
        max_length=150,
        blank=False,
        unique=True
    )

    description = models.TextField(
        verbose_name="説明",
        blank=False,
        unique=True
    )

    code = MDTextField(
        verbose_name="コード",
        blank=False,
        unique=True
    )

    image01 = models.ImageField(
        verbose_name="画像",
        blank=True,
        upload_to="images/",
    )

    image02 = models.ImageField(
        verbose_name="画像",
        blank=True,
        upload_to="images/",
    )

    image03 = models.ImageField(
        verbose_name="画像",
        blank=True,
        upload_to="images/",
    )

    image04 = models.ImageField(
        verbose_name="画像",
        blank=True,
        upload_to="images/",
    )

    def __str__(self):
        return str(self.name)

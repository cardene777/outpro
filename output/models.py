from django.db import models
from mdeditor.fields import MDTextField


class Output(models.Model):
    class Meta:
        verbose_name = "アウトプット"
        verbose_name_plural = "アウトプット"

    username = models.CharField(
        verbose_name="ユーザー名",
        max_length=100,
    )

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
        blank=False,
        upload_to="outpro_images/",
        default="images/default.jpg"
    )

    LANGUAGE_CHOICES = (
        ("Python", "Python"),
        ("PHP", "PHP"),
        ("JavaScript", "JavaScript"),
        ("Go", "Go"),
        ("Ruby", "Ruby"),
        ("Java", "Java"),
        ("HTML5", "HTML5"),
        ("CSS3", "CSS3"),
    )

    language = models.CharField(
        verbose_name="言語",
        choices=LANGUAGE_CHOICES,
        max_length=50
    )

    created_at = models.DateTimeField(
        verbose_name="作成日",
        blank=False,
        auto_now=True,
    )

    def __str__(self):
        return str(self.title)


class Program(models.Model):
    class Meta:
        verbose_name = "プログラム"
        verbose_name_plural = "プログラム"

    username = models.CharField(
        verbose_name="ユーザー名",
        max_length=100,
    )

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
        upload_to="outpro_images/",
    )

    image02 = models.ImageField(
        verbose_name="画像",
        blank=True,
        upload_to="outpro_images/",
    )

    image03 = models.ImageField(
        verbose_name="画像",
        blank=True,
        upload_to="outpro_images/",
    )

    image04 = models.ImageField(
        verbose_name="画像",
        blank=True,
        upload_to="outpro_images/",
    )

    good_count = models.IntegerField(
        verbose_name="いいね",
        default=0
    )

    created_at = models.DateTimeField(
        verbose_name="作成日",
        blank=False,
        auto_now=True,
    )

    review = models.BooleanField(
        verbose_name="レビュー",
        default=False
    )

    def __str__(self):
        return str(self.name)


class Good(models.Model):
    class Meta:
        verbose_name = "グッド"
        verbose_name_plural = "グッド"

    program = models.ForeignKey(
        Program,
        verbose_name="作品",
        on_delete=models.CASCADE
    )

    username = models.CharField(
        verbose_name="ユーザー名",
        max_length=100,
    )

    def __str__(self):
        return str(self.username)


class ReviewCode(models.Model):
    class Meta:
        verbose_name = "コードレビュー"
        verbose_name_plural = "コードレビュー"

    program_id = models.ForeignKey(
        Program,
        verbose_name="プログラムID",
        on_delete=models.CASCADE
    )

    username = models.CharField(
        verbose_name="ユーザー名",
        max_length=100
    )

    review_code = MDTextField()

    check = models.BooleanField(
        verbose_name="チェック済み",
        default=False,
        blank=True
    )

    def __str__(self):
        return str(self.program_id)


class Message(models.Model):
    class Meta:
        verbose_name = "メッセージ"
        verbose_name_plural = "メッセージ"

    review = models.ForeignKey(
        ReviewCode,
        verbose_name="レビューモデル",
        on_delete=models.CASCADE
    )

    username = models.CharField(
        verbose_name="ユーザー名",
        max_length=100
    )

    message = models.TextField(
        verbose_name="メッセージ"
    )

    check = models.BooleanField(
        verbose_name="メッセージチェック済み",
        default=False,
        blank=True
    )

    def __str__(self):
        return str(self.comment)


class Comment(models.Model):
    class Meta:
        verbose_name = "コメント"
        verbose_name_plural = "コメント"

    output_id = models.ForeignKey(
        Output,
        verbose_name="アウトプットID",
        on_delete=models.CASCADE,
        blank=True,
        default=0
    )

    program_id = models.ForeignKey(
        Program,
        verbose_name="プログラムID",
        on_delete=models.CASCADE,
        blank=True,
        default=0
    )

    username = models.CharField(
        verbose_name="ユーザー名",
        max_length=100
    )

    comment = models.TextField(
        verbose_name="コメント"
    )

    def __str__(self):
        return str(self.comment)



from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Disciplina(models.Model):
    name = models.CharField("Disciplina", max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplinas"


class Questao(models.Model):

    disciplines = models.ManyToManyField(
        'Disciplina', related_name='Disciplina', verbose_name="Disciplinas")
    theme = models.CharField(
        "Conteúdo", max_length=256, null=True, blank=False, help_text="Conteúdo abordado pela questão")
    grade = models.IntegerField(
        "Série", null=True, blank=False, help_text="Série para qual foi elaborada a questão")
    statement = RichTextUploadingField("Enunciado")

    uploaded_at = models.DateTimeField(
        "Adicionada em", auto_now_add=True, null=True)
    modified_at = models.DateTimeField(
        "Modificado em", auto_now=True, null=True)

    def __str__(self):
        return self.statement

    def get_disciplines(self):
        return ", ".join([p.name for p in self.disciplines.all()])

    get_disciplines.short_description = "Disciplinas"

    class Meta:
        verbose_name = "Questão"
        verbose_name_plural = "Questões"

from django.contrib import admin

from core.models import *

# Register your models here.


class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Disciplina, DisciplinaAdmin)


class QuestaoAdmin(admin.ModelAdmin):
    list_display = ['statement', 'get_disciplines',
                    'grade', 'theme', 'uploaded_at', 'modified_at']
    search_fields = ['statement', 'theme']
    list_filter = ['disciplines__name', 'grade']


admin.site.register(Questao, QuestaoAdmin)

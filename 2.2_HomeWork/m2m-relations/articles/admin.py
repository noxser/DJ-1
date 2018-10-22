from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scopes, MainScopes



class MainScopesInlineFormset(BaseInlineFormSet):
    def clean(self):
        check_box = 0
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            # form.cleaned_data
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
            # raise ValidationError('Тут всегда ошибка')

            if form.cleaned_data and form.cleaned_data['is_main']:
                check_box += 1
        if check_box == 0:
            raise ValidationError('Укажите основной раздел')
        if check_box > 1:
            raise ValidationError('Основным может быть только один раздел')
        return super().clean()  # вызываем базовый код переопределяемого метода

class MainScopesInline(admin.TabularInline):
    model = MainScopes
    formset = MainScopesInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at', 'display_tag')
    inlines = [MainScopesInline]

@admin.register(Scopes)
class ScopesAdmin(admin.ModelAdmin):
    pass



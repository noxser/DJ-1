from django.contrib import admin

from .models import Student, Teacher


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'group', 'display_teachers')
    list_filter = ('group', 'teacher')  # добавляем фильтры в админку

    # не работает вместе с fieldsets
    # fields = ['name', 'group', 'teacher']  # порядок полей в админке

    fieldsets = (
        (None, {
            'fields': ('name', 'group',)
        }),
        ('Учителя', {
            'fields': ('teacher',)
        }),
    )
    pass


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject')
    list_filter = ('subject', )  # добавляем фильтры в админку
    pass

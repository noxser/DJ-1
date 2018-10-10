from django.urls import register_converter, path
from datetime import datetime
from app.views import file_content, FileList

# Определите и зарегистрируйте конвертер для определения даты в урлах и наоборот урла по датам
class DateConverter:
    regex = '[0-9]{4}\-[0-9]{1,2}\-[0-9]{1,2}'
    # перехватываем строку из адреса и преобразовываем ее в дату
    def to_python(self, value):
        return datetime.strptime(value,"%Y-%m-%d").date()

    def to_url(self, value):
    	return value.date()


register_converter(DateConverter, 'dddd')

urlpatterns = [
    # Определите схему урлов с привязкой к отображениям .views.FileList и .views.file_content
    path('', FileList.as_view(), name='file_list'),
    path('<dddd:date>', FileList.as_view(), name='file_list'),
    path('file/<str:name>', file_content, name='file_content'),
]

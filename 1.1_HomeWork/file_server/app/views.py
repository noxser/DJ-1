import os
from datetime import datetime
from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView
from app.settings import FILES_PATH



class FileList(TemplateView):
    template_name = 'index.html'
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    def get_context_data(self, date=None):
        file_list = []
        rezult = {}
        files = os.listdir(FILES_PATH)
        for f in files:
            f_info = os.stat(os.path.join(FILES_PATH, f))
            if date == None or datetime.fromtimestamp(int(f_info.st_ctime)).date() <= date :
                file_list.append({
                    'name': f,
                    'ctime':datetime.fromtimestamp(int(f_info.st_ctime)), 
                    'mtime':datetime.fromtimestamp(int(f_info.st_mtime))
                    })
        rezult['files'] = file_list
        if date: rezult['date'] = date        
        return rezult


def file_content(request, name):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:

    # на случай  ошибки в имени файла
    try:
        with open(os.path.join(FILES_PATH, name), encoding='utf-8') as file:
            data = file.read()
    except Exception:
        data = 'File not found'

    return render_to_response(
        'file_content.html',
        context={'file_name':name, 'file_content': data}
    )


from django.views.generic import TemplateView
from django.shortcuts import render

from .forms import CalcForm


class CalcView(TemplateView):
    template_name = 'app/calc.html'

    def get(self, request, *args, **kwargs):
        form = CalcForm(self.request.GET or None)  # instance= None
        if form.is_valid():
            cost = int(self.request.GET['initial_fee'])
            rate = int(self.request.GET['rate'])
            months_count = int(self.request.GET['months_count'])

            common_result = round((cost + cost * rate) / months_count)
            result = round(common_result / months_count, 2)

            return render(request, self.template_name,
                          {'form': form, 'common_result': common_result, 'result': result})
        return render(request, self.template_name, {'form': form})


class CalcViewHandMaid(TemplateView):
    template_name = 'app/calc_hand_maid.html'

    def get(self, request, *args, **kwargs):
        if self.request.GET or None:
            form_data = {'no_err': True}

            def check_field(field_name):
                if not self.request.GET[field_name].isdigit():
                    form_data[f'{field_name}_err'] = 'Введите число!!!'
                    form_data['no_err'] = False
                else:
                    form_data[field_name] = int(self.request.GET[field_name])

            check_field('rate')  # проверяем поле rate
            check_field('cost')  # проверяем поле cost
            check_field('months_count')  # проверяем поле months_count

            if form_data['no_err']:
                common_result = round(
                    (form_data['cost'] + form_data['cost'] * form_data['rate']) / form_data['months_count'])
                result = round(common_result / form_data['months_count'], 2)
                form_data['common_result'] = common_result
                form_data['result'] = result

            return render(request, self.template_name, {'form_data': form_data})

        return render(request, self.template_name, )

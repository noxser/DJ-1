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
            result = round(common_result / 12, 2)
            print(result)
            print(common_result)

            return render(request, self.template_name,
                          {'form': form, 'common_result': common_result, 'result': result})
        return render(request, self.template_name, {'form': form})


class CalcViewHandMaid(TemplateView):
    template_name = 'app/calc_hand_maid.html'

    def get(self, request, *args, **kwargs):
        print(self.request.GET)
        if self.request.GET or None:
            cost = int(self.request.GET['initial_fee'])
            rate = int(self.request.GET['rate'])
            months_count = int(self.request.GET['months_count'])
            common_result = round((cost + cost * rate) / months_count)
            result = round(common_result / 12, 2)
            form_data = {'common_result': common_result,
                         'result': result,
                         'cost': cost,
                         'months_count': months_count,
                         'rate': rate}

            return render(request, self.template_name, {'form_data': form_data})

        return render(request, self.template_name, )

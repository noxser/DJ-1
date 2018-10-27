from django import forms


class CalcForm(forms.Form):
    initial_fee = forms.IntegerField(label="Стоимость товара")
    rate = forms.IntegerField(label="Процентная ставка")
    months_count = forms.IntegerField(label="Срок кредита в месяцах")

    def clean_initial_fee(self):
        # валидация одного поля, функция начинающаяся на `clean_` + имя поля
        initial_fee = self.cleaned_data.get('initial_fee')
        if not initial_fee or initial_fee < 1:
            raise forms.ValidationError("Стоимость товара не может быть отрицательной")
        return initial_fee

    def clean(self):
        # cleaned_data = super(CalcForm, self).clean()
        cleaned_data = super().clean()
        rate = cleaned_data.get('rate')
        months_count = cleaned_data.get('months_count')

        if not rate or rate < 1:
            self.add_error('rate', "Процентная ставка не может быть отрицательной")

        if not months_count or months_count < 1:
            self.add_error('months_count', "Срок кредита не может быть отрицательным")


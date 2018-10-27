from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.shortcuts import HttpResponseRedirect, get_object_or_404


from .models import Product, Review
from .forms import ReviewForm


class ProductsList(ListView):
    model = Product
    context_object_name = 'product_list'


class ProductView(DetailView):
    model = Product
    template_name = 'app/product_detail.html'

    def get_object(self):
        return get_object_or_404(Product, pk=self.kwargs.get(self.pk_url_kwarg, None))

    def get_context_data(self, **kwargs):
        current_product = self.get_object()
        context = super().get_context_data(**kwargs)
        context['form'] = ReviewForm
        context['reviews'] = Review.objects.filter(product=current_product)
        if self.request.session.get('has_commented_product', False):
            context['has_commented_obj'] = self.request.session.get('has_commented_product')
            if self.kwargs.get(self.pk_url_kwarg, None) in self.request.session.get('has_commented_product', []):
                context['is_review_exist'] = True
        return context


    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        current_product = Product.objects.get(id=pk)
        form = ReviewForm(self.request.POST)
        has_commented_product= self.request.session.get('has_commented_product', [])
        if form.is_valid() and pk not in has_commented_product:
            Review.objects.create(text=request.POST['text'], product=current_product)
            has_commented_product.append(pk)
            self.request.session['has_commented_product'] = has_commented_product
            return HttpResponseRedirect(reverse('product_detail', kwargs={'pk': pk}))
        return HttpResponseRedirect(reverse('product_detail', kwargs={'pk': pk}))



    #  # Уже было решение )))
    #
    # def get_success_url(self):
    #     product_id = self.request.session.get('current_product')
    #     if product_id:
    #         return reverse('product_detail', kwargs={'pk': product_id})
    #
    #     return reverse('main_page')
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     current_product = self.get_object()
    #     self.request.session['current_product'] = current_product.id
    #     context['reviews'] = Review.objects.filter(product=current_product)
    #     context['form'] = ReviewForm
    #
    #     reviewed_products = self.request.session.get('reviewed_products', [])
    #     context['is_review_exist'] = bool(current_product.id in reviewed_products)
    #     return context
    #
    # def post(self, request, *args, **kwargs):
    #     current_product_id = self.request.session['current_product']
    #     reviewed_products = self.request.session.get('reviewed_products', [])
    #
    #     if 'text' in request.POST and current_product_id and current_product_id not in reviewed_products:
    #         text_review = request.POST['text']
    #         current_product = Product.objects.get(id=current_product_id)
    #         Review.objects.create(text=text_review, product=current_product)
    #
    #         reviewed_products.append(current_product_id)
    #         self.request.session['reviewed_products'] = reviewed_products
    #     return redirect(self.get_success_url())

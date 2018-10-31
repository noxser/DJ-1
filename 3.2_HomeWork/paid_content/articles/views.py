from django.shortcuts import render
from .models import Article
from django.shortcuts import redirect


def show_articles(request):
    context = Article.objects.all()

    if request.user.is_authenticated:
        if request.user.profile.has_subscription:
            context = context
        else:
            context = context.filter(is_paid=False)
    else:
        context = context.filter(is_paid=False)

    return render(
        request,
        'articles.html', {'context': context}
    )


def show_article(request, id):
    # если юзер не имет подписку а получил линк на платную статью гоним на главную )
    cur_user = request.user
    if cur_user.is_authenticated:
        if cur_user.profile.has_subscription:
            context = Article.objects.get(pk=id)
        else:
            if Article.objects.get(pk=id).is_paid:
                return redirect('/articles/')
            else:
                context = Article.objects.get(pk=id)
    else:
        if Article.objects.get(pk=id).is_paid:
            return redirect('/articles/')
        else:
            context = Article.objects.get(pk=id)

    return render(
        request,
        'article.html', {'context': context}
    )


def by_subscription(request):
    cur_user = request.user
    if request.method == 'POST':
        if request.POST.get('sub'):
            cur_user.profile.has_subscription = True
        else:
            cur_user.profile.has_subscription = False
    cur_user.save()

    return render(
        request,
        'bye_subscription.html',
    )

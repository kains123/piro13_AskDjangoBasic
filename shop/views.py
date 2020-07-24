import logging
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Item

logger = logging.getLogger(__name__) #__name__은 shop.views안으로 들어간다.

def archives_year(request, year):
    return HttpResponse('{}년도에 대한 내용'.format(year))

def item_list(request):
    qs = Item.objects.all()

    q = request.GET.get('q', '')

    if q:
        qs = qs.filter(title__icontains=q)
    logger.debug('query : {}'.format(q))
    return render(request, 'shop/item_list.html', {
        'item_list': qs,
        'q': q
    })

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'shop/item_detail.html', {
            'item': item,
    })
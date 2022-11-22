import re

from django.core.handlers.wsgi import WSGIRequest
from django.http import Http404
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from main.models import ServiceRequest


@require_http_methods(['GET', 'POST'])
def main_page_view(request: WSGIRequest):
    """View для обработки главной страницы"""
    if request.method == 'GET':
        return render(request, 'main/index.html')

    car_name = request.POST.get('brand')
    year = request.POST.get('year')
    volume = request.POST.get('volume')
    phone = request.POST.get('phone')

    service = ServiceRequest(car_model_name=car_name, car_production_year=year, engine_volume=volume, phone=phone)
    service.save()

    return render(request, 'main/index.html')


def admin_page(request: WSGIRequest):
    if not request.user.is_staff:
        raise Http404

    all_services = ServiceRequest.objects.order_by('-dt_created')

    return render(request, 'main/admin_page.html', {'all_services': all_services})
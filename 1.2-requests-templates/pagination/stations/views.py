import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open(BUS_STATION_CSV, encoding='UTF-8') as csvfile:
        reader = list(csv.DictReader(csvfile))
        paginator = Paginator(reader, 10)
        page_number = int(request.GET.get("page", 1))
        page = paginator.get_page(page_number)
        context = {
            'bus_stations': page,
            'page': page,
        }
    return render(request, 'stations/order.html', context)

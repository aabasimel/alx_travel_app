from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to Listings!")

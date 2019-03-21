from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import Button

@login_required()
def home(request):
    """
    Controller for the app home page.
    """

    context = {
    }

    return render(request, 'arcgis_test/home.html', context)

@login_required()
def watershed(request):
    """
    Controller for the app home page.
    """

    context = {
    }

    return render(request, 'arcgis_test/watershed.html', context)
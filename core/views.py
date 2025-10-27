# core/views.py
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    """Render the index page."""
    return render(request, "core/index.html", {})


def health_view(request: HttpRequest) -> HttpResponse:
    """Simple health endpoint used by uptime checks."""
    return render(request, "health.html", {})

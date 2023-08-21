from django.http import HttpResponse

# Create your views here.
dev index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

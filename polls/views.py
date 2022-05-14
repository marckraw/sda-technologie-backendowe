from django.http import HttpResponse

def hello(request, year):
    return HttpResponse(f"Hello, world! {year}")

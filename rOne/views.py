from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("rOne says hey there world!")

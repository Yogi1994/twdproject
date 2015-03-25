from django.http import HttpResponse
import os
from django.shortcuts import render
# Create your views here.
def index(request):

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am bold font from the context"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'rOne/index.html', context_dict)

def about(request):
    return HttpResponse("rOne About.<br /><a href='/rOne/'>Index</a>")

'''def index(request):
    return HttpResponse("rOne says hey there world!")
'''

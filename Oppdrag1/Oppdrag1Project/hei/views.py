

from django.http import HttpResponse
from django.template import loader
# Create your views here.

def hei(request):
    template = loader.get_template('hei.html')
    return HttpResponse(template.render())
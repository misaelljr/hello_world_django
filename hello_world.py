from django.conf.urls import url
from django.http import HttpResponse

SECRET_KEY = 'hello_world'
DEBUG = True
ROOT_URLCONF = __name__

def hello_world(request):
	return HttpResponse('Software Reuse - Hello World!')

urlpatterns = [
	url(r'^$', hello_world)
]
import importlib
import sys
from django.conf import settings
from django.core.management import execute_from_command_line
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import path
settings.configure(
	ROOT_URLCONF=__name__,
	DEBUG=True,
	SECRET_KEY='secret',
	TEMPLATES=[
		{
			'BACKEND': 'django.template.backends.django.DjangoTemplates',
			'DIRS': ['C:\\Users\\User\\PycharmProjects\\hillel1\\html'],
		}
	]
)


# 1
def easter_egg(_):
	return HttpResponse('You Found Easter Egg congratulation!!!')


def header(request, name_of_module):
	try:
		list_of_modules = [i for i in dir(importlib.import_module(name=f'{name_of_module}')) if not i.startswith('_')]
		return render(request, 'index.html', {'string': list_of_modules})
	except ModuleNotFoundError:
		return HttpResponse(f"No module named '{name_of_module}'")


def doc_of_function(_, name_of_module, name):
	return HttpResponse(getattr(importlib.import_module(name=f'{name_of_module}'), name).__doc__)

# 2
dict1 = {}

def search(request):
	url = request.POST.get('req','')
	massage = 'Invalid URL . Allowed schemes: http,ftp,https'
	short_url = p()
	if url.startswith(('http://','https://','ftp://')):
		dict1[short_url] = url
		massage = short_url
	return render(request, 'zen.html', {'message': massage, 'check': len(massage)})

def redirect(request,key):
	return HttpResponseRedirect(dict1[key])



urlpatterns = [
	path('', search),
	path('<key>', redirect),
	path('doc', easter_egg),
	path('doc/<name_of_module>', header),
	path('doc/<name_of_module>/<name>', doc_of_function)
]
if __name__ == '__main__':
	execute_from_command_line(sys.argv)
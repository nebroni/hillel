import importlib
import sys
from django.conf import settings
from django.core.management import execute_from_command_line
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path
settings.configure(
	ROOT_URLCONF = __name__,
	DEBUG = True,
	SECRET_KEY = 'secret',
	TAMPLATES = [
		{

		}
	]
)
html_file = """
<!DOCTYPE html>
<html>
<head>
<title>Nebroni</title>
</head>
<body>
{string}
<h2>@nebroni</h2>
</body>
</html>
"""


def easter_egg(_):
	return HttpResponse('You Found Easter Egg congratulation!!!')


def header(request, name_of_module):
	try:
		list_of_modules = [i for i in dir(importlib.import_module(name=f'{name_of_module}')) if not i.startswith('_')]
		return render(request, 'index.html', {'string':list_of_modules}) #HttpResponse(html_file.format(string=string_of_modules))
	except ModuleNotFoundError:
		return HttpResponse(f"No module named '{name_of_module}'")


def doc_of_function(_, name_of_module, name):
	return HttpResponse(getattr(importlib.import_module(name=f'{name_of_module}'), name).__doc__)


urlpatterns = [
	path('doc', easter_egg),
	path('doc/<name_of_module>', header),
	path('doc/<name_of_module>/<name>', doc_of_function)
]
if __name__ == '__main__':
	execute_from_command_line(sys.argv)
import importlib
import sys
import this
import random
from django.core.management import execute_from_command_line
from django.conf import settings
from django.http import HttpResponse
from django.urls import path



settings.configure(
ROOT_URLCONF = __name__,
DEBUG = True,
SECRET_KEY = 'secret'
)


list_of_modules = [i for i in dir(importlib.import_module(name='random')) if not i.startswith('_')]
string_of_modules = '\n'.join([f'<a href="random/{i}">{i}</a><br>' for i in list_of_modules])



html_file = f"""
<!DOCTYPE html>
<html>
<head>
<title>Nebroni</title>
</head>
<body>
{string_of_modules}
<h2>@nebroni</h2>
</body>
</html>
"""

def hello(_):
	return HttpResponse(html_file)

urlpatterns = [

	path('random', hello)
]

execute_from_command_line(sys.argv)


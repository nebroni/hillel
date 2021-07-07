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

text = ''.join([this.d.get(i,i) for i in this.s])
title, _, *quotes = text.split('\n')

html_file = """
<!DOCTYPE html>
<html>
<head>
<title>{title}</title>
</head>
<body>
<h1>{quote}</h1>
<h2>@nebroni</h2>
</body>
</html>
"""

def hello(_):
	return HttpResponse(html_file.format(title = title, quote = random.choice(quotes)))

urlpatterns = [
	path('',hello)
]

execute_from_command_line(sys.argv)


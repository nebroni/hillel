import importlib
from password import password as p
from django.core.management import execute_from_command_line
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import path
from pathlib import Path
from django.db import connection

BASE_DIR = Path(__file__).resolve().parent

ROOT_URLCONF = __name__
DEBUG = True
SECRET_KEY = 'secret'
TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': ['html'],
	},
]
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': BASE_DIR / 'database.sqlite3'
	}
}


# CREATE TABLE
command_create = 'create table if not exists table_key (key char(5), link text)'
with connection.cursor() as cur:
	cur.execute(command_create)


# INSERT TABLE
def insert_table(key, link):
	with connection.cursor() as cur:
		command_insert = f'insert into table_key (key, link) values (%s, %s);'
		cur.executemany(command_insert, [[key, link]])


# DELETE TABLE
def delete_table():
	with connection.cursor() as cur:
		cur.execute('delete from table_key')


# 1

def header(request, name_of_module):
	try:
		list_of_modules = [i for i in dir(importlib.import_module(name=f'{name_of_module}')) if not i.startswith('_')]
		return render(request, 'index.html', {'string': list_of_modules, 'name_of_module': name_of_module})
	except ModuleNotFoundError:
		return HttpResponse(f"No module named '{name_of_module}'")


def doc_of_function(_, name_of_module, name):
	return HttpResponse(getattr(importlib.import_module(name=f'{name_of_module}'), name).__doc__)


# 2

def search(request):
	url = request.POST.get('req', '')
	message = 'Invalid URL. Allowed schemes: http,ftp,https'
	short_url = p()
	if url.startswith(('http://', 'https://', 'ftp://')):
		insert_table(short_url, url)
		message = short_url
	return render(request, 'zen.html', {'message': message * bool(url), 'check': len(message)})


def redirect(_, key):
	if key == 'doc':
		return HttpResponse('You found easter egg)')
	with connection.cursor() as cur:
		command = f'select link from table_key where key="{key}"'
		cur.execute(command)
		ans = cur.fetchone()
		if ans:
			return HttpResponseRedirect(ans[0])
		else:
			return HttpResponseRedirect('/')


urlpatterns = [
	path('', search),
	path('<key>', redirect),
	path('doc/<name_of_module>', header),
	path('doc/<name_of_module>/<name>', doc_of_function)
]

if __name__ == '__main__':
	execute_from_command_line()
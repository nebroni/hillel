import importlib
import random
ans = []
print(random.choice.__doc__)
print(getattr(random, 'random'))
print(dir(importlib.import_module(name='random')))
list_of_modules = [i for i in dir(importlib.import_module(name='random')) if not i.startswith('_')]
string_of_modules = '\n'.join([f'<a href="random/{i}">{i}</a>' for i in list_of_modules])
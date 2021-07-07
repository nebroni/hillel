import importlib
import random
ans = []
print(random.choice.__doc__)
print(dir(getattr(random, 'choice')))
for i in dir(importlib.import_module(name='random')):
	if '_' not in i:
		print(i)
	else:
		ans.append(i)
print(ans)

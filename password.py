import string
import random


def password():
	password = random.sample(
		[random.choice(string.digits), random.choice(string.ascii_lowercase), random.choice(string.ascii_uppercase)], 3)
	password += random.sample(string.ascii_letters + string.digits, 2)
	return ''.join(password)

import string
import random

from django.shortcuts import render
from landind_app.settings import ALLOWED_HOSTS


def index(request):
    return render(request, 'core/index.html')


def gen_password():
    password = ''
    for _ in range(10):
        letter = random.choice(string.ascii_lowercase)
        password += letter
    for _ in range(3):
        letter = random.choice(string.ascii_uppercase)
        password += letter

    for _ in range(2):
        digit = random.choice(string.digits)
        password += digit
    list_password = list(password)
    new_password = ''
    for i in range(15):
        index = random.choice(range(len(list_password)))
        letter = list_password.pop(index)
        new_password += letter

    return new_password


def generate_password(request):
    password = gen_password()
    url = 'http://' + ALLOWED_HOSTS[0] + '/generate-password'
    return render(request, 'core/password_created.html', context={
        'password': password,
        'url': url
    })
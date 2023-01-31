from django.shortcuts import render
from django.http import HttpResponse
import random
import string

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):
    # Recieve the password preferences
    preferences = getPasswordParams(request)
    length = preferences["length"]
    characters = preferences["characters"]
    
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})

def getPasswordParams(request):
    # check password length
    length = int(request.GET.get('length',10))

    # check case preferences
    if request.GET.get('uppercase') == 'on':
        characters = list(string.ascii_letters)
    else:
        characters = list(string.ascii_lowercase)

    # check for special characters
    if request.GET.get('special') == 'on':
        special = list(string.punctuation)
        characters = characters + special
    
    # check for numbers
    if request.GET.get('numbers') == 'on':
        digits = list(string.digits)
        characters = characters + digits
    
    result = {"length":length, "characters":characters}

    return result

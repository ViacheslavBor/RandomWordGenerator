from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string

def index(request):
	return render(request, "aps/word.html")

def random_word(request):
	request.session["id"] = get_random_string(length=14)
	if "count" in request.session:
		request.session["count"] += 1
	else: 
		request.session["count"] = 1
	return redirect('/')
	
def reset(request):
	request.session["count"] = 0
	request.session["id"] = ""
	return redirect('/')
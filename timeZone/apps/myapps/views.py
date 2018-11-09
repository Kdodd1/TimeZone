from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
	context = {
		#Oct 26, 2013 11:2
		"time": strftime("%b %d, %Y \n %H: %M %p")
	}

	return render(request, "myapps/index.html", context)
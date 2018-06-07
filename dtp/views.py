#from django.http import HttpResponse
from django.shortcuts import render
def home(request):
	#return  HttpResponse("<h1>hello dtp</h1>")
	return render(request,'home.html')

def about(request):
	#return  HttpResponse("<h1>hello dtp</h1>")
	return render(request,'pages/about.html')

def contact(request):
	#return  HttpResponse("<h1>hello dtp</h1>")
	return render(request,'pages/contact.html')
from django.shortcuts import render

# Create your views here.

template_name = 'test.html'


def qrview(request):
	return render(request, template_name)


def qrview1(request):
	template_name = 'test1.html'
	return render(request, template_name)


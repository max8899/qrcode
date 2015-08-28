from django.shortcuts import render

# Create your views here.

template_name = 'test.html'


def qrview(request):
	return render(request, template_name)


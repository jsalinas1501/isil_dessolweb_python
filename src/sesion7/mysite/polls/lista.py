from django.http import HttpResponse

def lista(request):
	x=list(range(1, 101))
	return HttpResponse(x, "")
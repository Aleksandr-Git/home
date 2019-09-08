#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
 
def index(request):
    f = open('/home/aleksandr/test_1/help/help.txt', 'r')
    page = ''
    flag = False
    for line in f:
        if flag == False:
            page += '<p><b>' + line + '</b></p>'
            flag = True

        else:
            page += '<p><i><font color="red">' + line + '</font></i></p>'
            flag = False
    f.close()
    return HttpResponse(page)
#    return HttpResponse("<!DOCTYPE HTML>" + "<b>Hello World!</b>" + "<p> Test</p>")

def home(request):
	roof = '0000'
	data = {"mode": "non", "roof": roof, "neptun": "non", "power": "non", "security": "non"}
	return render(request, "home.html", context=data)
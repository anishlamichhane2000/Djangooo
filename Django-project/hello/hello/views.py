
# Views.py
# I have created this file - anish
from django.http import HttpResponse
from django.shortcuts import render




def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")



def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')
    #check  checkbox  value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps =  request.POST.get('fullcaps', 'off')
    newlineremover =  request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    #check which check box is on

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed +char.upper()
        params = {'purpose':'Changed to uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char !="n" and char !="\r":
                analyzed = analyzed +char
        params = {'purpose':'Removed new lines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1]==""):
                analyzed = analyzed +char
        params = {'purpose':'Removed new lines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Error")
def ex1(request):
    s = ''' <h1>Naviagtion bar<h1><br>
    <a href = "https://www.youtube.com/watch?v=7ahtjFMGpWM">Youtube</a><br>
    <a href = "https://www.facebook.com">Facebook</a><br>
    <a href = "https://www.linkedin.com">Linkedin</a><br>
    <a href = "https://www.instagram.com">instagram</a><br>
    <a href = "https://www.espncricinfo.com">CricInfo</a><br>'''
    return HttpResponse(s)

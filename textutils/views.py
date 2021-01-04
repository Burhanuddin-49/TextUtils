# i have created this file- BB49
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index1.html')
    # return HttpResponse("Home")


def analyze(request):
    # GET THE TEXT
    djtext = request.POST.get('text', 'default')


    # check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    #check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed punctuations', 'analyzed_text': analyzed}
        djtext = analyzed


    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed


    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char

        params = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}
        djtext = analyzed


    if (extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}


    if(removepunc!="on" and newlineremover!="on" and fullcaps!="on" and extraspaceremover!="on"):
        return HttpResponse("Please select any opertions and try again ")


    return render(request, 'analyze.html', params)



# def capfirst(request):
#    return HttpResponse("capitalize first")


# def newlineremove(request):
 #   return HttpResponse("new line remover ")


# def spaceremove(request):
#    return HttpResponse("space remover <a href='/'>back</a>")


# def charcount(request):
#    return HttpResponse("charcount")

from django.http import HttpResponse
from django.shortcuts import redirect, render


def index(request):
    return render(request, 'index2.html')


def analyze_text(request):
    text_to_be_analyzed = request.POST.get('textget', 'default')
    remove_punctuation = request.POST.get('removePunc', "no")
    capitalization = request.POST.get('enableCapitalization', 'no')
    lower_capitalization = request.POST.get('enablelCapitalization', 'no')
    format_text = request.POST.get('enableFormattext', 'no')
    extra_spacing = request.POST.get('enableExtraspacing', 'no')

    print(capitalization)
    punctuation = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

    analyzed_text = ''
    counter = ''
    if remove_punctuation == 'on':
        for char in text_to_be_analyzed:
            if char not in punctuation:
                analyzed_text = analyzed_text + char
        result = {'analyze': analyzed_text,'yes':True}
        text_to_be_analyzed = analyzed_text

    if capitalization == 'on':
        analyzed_text = text_to_be_analyzed.upper()
        result = {'analyze': analyzed_text}
        text_to_be_analyzed = analyzed_text
        
    if lower_capitalization == 'on':
        analyzed_text = text_to_be_analyzed.lower()
        result = {'analyze': analyzed_text,'yes':True}
        text_to_be_analyzed = analyzed_text


    
    if extra_spacing == 'on':
        new_text = ''
        for i in range(0,len(text_to_be_analyzed),1):
            if(i+1 < len(text_to_be_analyzed)):
                if text_to_be_analyzed[i]==' ' and text_to_be_analyzed[i+1]==' ':
                    pass
                else:
                    new_text = new_text + text_to_be_analyzed[i]
        analyzed_text = new_text
        result = {'analyze': analyzed_text,'yes':True}
        text_to_be_analyzed = analyzed_text
        
    if format_text == 'on':
        text_to_be_analyzed = text_to_be_analyzed.split('. ')
        formatted_text = ''
        for word in text_to_be_analyzed:
            formatted_text =formatted_text + word[0].upper()
            formatted_text = formatted_text + word[1:]
            if word[-1]!='.':
                print(word[-1])
                formatted_text = formatted_text + '. '
        result = {'analyze': formatted_text,'yes':True} 
    
    if remove_punctuation!='on' and capitalization!='on' and  lower_capitalization!='on' and extra_spacing!='on' and format_text!='on':
        return render(request,'index2.html',{'no':True}) 
    return render(request, 'analyzed_text.html', result)


def output(request):
    return render(request,'analyzed_text.html')
    
from django.shortcuts import render,get_object_or_404
from .models import FAQ
from .models import QNA
# Create your views here.

def showmain(request):
    return render(request, 'app1_simbathon5/index.html')

def frequentlyaskedquestions(request):
    faqs = FAQ.objects.all()
    return render(request, 'app1_simbathon5/FAQ.html',{'faqs':faqs})

def detail(request,id):
    faq = get_object_or_404 (FAQ, pk = id)
    return render(request, 'app1_simbathon5/FAQ.html',{'faq':faq})

def book(request):
    return render(request, 'app1_simbathon5/book.html')
    
def main(request):
    return render(request, 'app1_simbathon5/main.html')

    
def qnaView(request):
    template_name = 'app1_simbathon5/Q&A.html'
    qna_object = QNA.objects.all()
    context = {
        'qnaobject':qna_object
    }
    return render(request, template_name, context)

   
    

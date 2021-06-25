from django.urls import path,include
from django.contrib import admin
from .views import *
from app1_simbathon5 import views
from app1_simbathon5.views import qnaView

app_name = "app1_simbathon5"
urlpatterns = [
    path('', main, name= "main"),
    path('FAQ/', frequentlyaskedquestions , name= "frequentlyaskedquestions"),
    path('<str:id>', views.detail, name="detail"),
    path('book/', book,name="book"),
    path('showmain/',showmain,name="showmain"),
    path('view/', qnaView), 
    path('admin/', admin.site.urls),
    path('Q&A/', qnaView, name= "qnaview"),

]

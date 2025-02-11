from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
import pandas as pd
from django.http import HttpResponse
from .models import Book 


# Create your views here.
@login_required
def home(request):
    return render(request, "home.html")

def base(request):
    return render(request, "base.html")

def about(request):
    return render(request, "about.html")

def enquiry(request):
    frm = EnquiryForm()
    return render(request, "enquiry.html", {'form':frm})

def student(request):
    if request.method == 'POST':
        fm = StudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('home')
    else:   
        form = StudentForm()
    return render(request, "student.html", {'form':form})

def test(request):
    if request.method == 'POST':
        name = request.POST.get('nm')
        age = request.POST.get('ag')
        ad = request.POST.get('ad')
        depart = request.POST.get('dp')
        s = Student(name=name, age=age, ad_num=ad, department=depart)
        s.save()
        return redirect('home')
    else:
        return render(request, "test.html")


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            usr = form.save(commit=False)
            raw_password = form.cleaned_data.get('password')
            usr.set_password(raw_password)
            usr.save()
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, "register.html", {'form':form})

def uslogn(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, "login.html", {'form':form})

def uslogout(request):
    logout(request)
    return redirect ('uslogn')


def book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book_instance = form.save()

            # Email Content
            subject = "New Book Submission"
            message = f"""
            A new book has been submitted.
            
            Title: {book_instance.title}
            Author: {book_instance.author}
            Submitted Successfully!
            """
            recipient_list = ['aryajanardhanan45@gmail.com']

            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)

            return redirect('bookdetails')
    else:
        form = BookForm()
    return render(request, "add.html", {'form':form})

def bookdetails(request):
    bk = Book.objects.all()
    return render(request, "books.html",{'book':bk} )


def bookdownload(request):
    bk = Book.objects.all()
    data = list(bk.values())
    df = pd.DataFrame(data)

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="books.xlsx"'

    with pd.ExcelWriter(response, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Books')
    return response 


def delt(request, pk):
    item = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('bookdetails')


def editt(request, pk):
    item = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('bookdetails')
    else:
        form = BookForm(instance=item)
    return render(request, "edit.html", {'form':form})


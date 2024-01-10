from django.shortcuts import render,redirect,HttpResponse
from .models import book
from .forms import bookForm
from django.db.models import Q
from django.contrib.auth.models import User
# Create your views here.


def home(request):
    return render(request, 'index.html')


def view_book(request):
    books = book.objects.all()
    return render(request, 'Bview.html', {'books': books})


def add_book(request):

    return render(request, 'Badd.html')


def add_book2(request):
    if request.method == "POST":
        form = bookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return home(request)
    form = bookForm()
    return render(request, 'add2.html', {'form': form})


def book_detail(request, p):
    b = book.objects.get(id=p)
    return render(request, 'book_detail.html', {'b': b})


def book_delete(request, p):
    b = book.objects.get(id=p)
    b.delete()
    return view_book(request)


def book_edit(request, p):
    b = book.objects.get(id=p)

    # b.delete()
    return render(request, 'Badd.html', {'b': b})


def search_view(request):
    # b=book.objects.get(id=p)
    # b.delete()
    # if request.method=="POST":

    return render(request, 'search.html')


def search(request):
    query = ""
    b = None
    if request.method == "POST":
        query = request.POST['search_for']
        if query:
            b = book.objects.filter(
                Q(title__icontains=query) | Q(author__icontains=query))
        return render(request, 'search.html', {'query': query, 'b': b})
        # b = book.objects.filter(Q(title=request.POST['search_for']) | Q(author=request.POST['search_for']))


def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        password2=request.POST['password2']
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        email=request.POST['email']
        if password==password2:
            u=User.objects.create_user(username=username,password=password,first_name=firstname,last_name=lastname,email=email)
            u.save()
            return redirect('books:home')
        else:
            return HttpResponse('passwords not same')

        

    return render(request, 'register.html')

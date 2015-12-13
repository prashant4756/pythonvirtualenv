from django.shortcuts import render
from .models import Books,Library
from .forms import BooksForm
from django.shortcuts import redirect
# Create your views here.
def post_list(request):
	books=Books.objects.all()
	librarys=Library.objects.all()
	return render(request,'firstblog/post_list.html',{'librarys' : librarys,'books': books})

def librarydetails(request,pk):
	library=Library.objects.get(pk=pk)
	books=library.books_set.all()
	return render(request,'firstblog/librarydetails.html',{'books': books})	

def new_add(request):
	if request.method=='GET':
		form=BooksForm()
	else:
		form=BooksForm(request.POST)
		if form.is_valid():
			obj=form.save(commit=False)
			obj.save()
			return redirect('/',pk=obj.pk)
	return render(request,'firstblog/new/addnewbook.html',{'form':form})

from django import forms
from firstblog.models import Books,Library

class BooksForm(forms.ModelForm):
	class Meta:
		model=Books
		fields=('bookName','library',)
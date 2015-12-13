from django.contrib import admin
from .models import Books
from .models import Library

admin.site.register(Books)
admin.site.register(Library)
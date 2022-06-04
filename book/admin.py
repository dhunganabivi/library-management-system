from django.contrib import admin
from book.models import Books, Student, Staff, Library_details

# Register your models here.
admin.site.register(Books)
admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(Library_details)


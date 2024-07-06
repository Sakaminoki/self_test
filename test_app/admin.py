from django.contrib import admin

# Register your models here.

from test_app.models import BookInfo,PeopleInfo

admin.site.register(BookInfo)
admin.site.register(PeopleInfo)
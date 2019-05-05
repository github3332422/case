
from django.contrib import admin
from TestModel.models import Test,Contact#,Tag
# # Register your models here.
# from TestModel.models import Test
# from TestModel.models import Contact
# # from TestModel.models import Tag
admin.site.register([Test, Contact])
# # Register your models here.
# admin.site.register(Test)

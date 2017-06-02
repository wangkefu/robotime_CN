from django.contrib import admin

# Register your models here.
from robotime_cn_website.models import RtProduct,Group,Category

admin.site.register(RtProduct)
admin.site.register(Group)
admin.site.register(Category)
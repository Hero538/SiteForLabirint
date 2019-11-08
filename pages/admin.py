from django.contrib import admin
from .models import Tiding
# Register your models here.
class TidingAdmin(admin.ModelAdmin):
    list_display = ('id','title','is_published','pub_date')
    list_display_links = ('id','title')
    list_filter = ('title',)
    list_editable = ('is_published',)
    search_fields = ('id','title')
    list_per_page = 15
admin.site.register(Tiding,TidingAdmin)
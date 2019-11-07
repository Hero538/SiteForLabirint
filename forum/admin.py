from django.contrib import admin
from .models import Post,Comment
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title','is_published','pub_date')
    list_display_links = ('id','title')
    list_filter = ('title',)
    list_editable = ('is_published',)
    search_fields = ('id','title')
    list_per_page = 15
admin.site.register(Post,PostAdmin)
admin.site.register(Comment)

from django.contrib import admin
from .models import Snippet
# Register your models here.
class SnippetAdmin(admin.ModelAdmin):
  list_display = ['title', 'code', 'description', 'created_by','created_at','updated_at']

admin.site.register(Snippet, SnippetAdmin)
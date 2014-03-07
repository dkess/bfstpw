from django.contrib import admin
from bfstpw.models import ForumThread, ForumPost

class ForumPostInline(admin.StackedInline):
    model = ForumPost
    
class ForumThreadAdmin(admin.ModelAdmin):
    fields = ['thread_title']
    inlines = [ForumPostInline]

admin.site.register(ForumThread,ForumThreadAdmin)

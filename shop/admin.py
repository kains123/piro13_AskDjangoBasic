from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'short_desc', 'price', 'is_publish']
    list_display_links = ['name']
    search_fields = ['name']
    #검색 기능도 넣을 수 있다. 
    list_filter = ['is_publish', 'updated_at']
    #필터도 설정 가능하다 
    def short_desc(self, item):
        return


from django.contrib import admin
from .models import TodoList, BoardList


# Register your models here.
# admin.site.register(TodoList)
# admin.site.register(BoardList)

class ListEntryAdmin(admin.ModelAdmin):
    list_display = ('item', 'userid', 'board_id')
    # search_fields = ['title']


class BoardEntryAdmin(admin.ModelAdmin):
    list_display = ('board_name', 'userid')


admin.site.register(TodoList, ListEntryAdmin)
admin.site.register(BoardList, BoardEntryAdmin)

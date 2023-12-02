from django.contrib import admin
from .models import ToDo

# Register your models here.
class ToDoAdmin(admin.ModelAdmin):
    list_display = ('sno' , 'task' , 'completed')
    list_filter = ('completed',)
    search_fields = ('sno , task',)


admin.site.register(ToDo , ToDoAdmin)

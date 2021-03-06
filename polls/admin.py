from polls.models import Poll
from polls.models import Choice
from django.contrib import admin

# admin.site.register(Poll)
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question']
    list_display = ('question', 'pub_date', 'was_published_recently')
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question']
    date_heirarchy = 'pub_date'

admin.site.register(Poll, PollAdmin)
#admin.site.register(Choice)

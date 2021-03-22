from django.contrib import admin

from api.models import Word, DictionaryEntry, Definition

class DefinitionAdmin(admin.StackedInline):
    model = Definition

class WordInline(admin.StackedInline):
    model = Word
    radio_fields = {'language': admin.HORIZONTAL}
    min_num = 2
    extra = 0


class DictionaryEntryAdmin(admin.ModelAdmin):
    fieldsets = (
      ('International Phonetic Alphabet', {
        'fields': ['ipa']
      }),
    )
    list_display = ['get_word']
    inlines = [WordInline]

    def get_word(self, obj):
        return obj.ipa;


admin.site.register(DictionaryEntry, DictionaryEntryAdmin)

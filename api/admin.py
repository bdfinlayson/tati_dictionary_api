from django.contrib import admin

from api.models import Word, DictionaryEntry, GrammaticalCategory

class WordInline(admin.StackedInline):
    model = Word
    radio_fields = {'language': admin.HORIZONTAL}
    min_num = 2
    extra = 0

class GrammaticalCategoryAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)
    search_fields = ('name',)

class DictionaryEntryAdmin(admin.ModelAdmin):
    fields = ('ipa', 'grammatical_category')
    list_display = ('get_words', 'get_grammatical_category', 'get_definitions',)
    search_fields = ('words__text', 'grammatical_category__name', 'definitions__text')
    inlines = [WordInline]

    # get_form controls how select options are labeled
    def get_form(self, request, obj=None, **kwargs):
        form = super(DictionaryEntryAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['grammatical_category'].label_from_instance = lambda obj: obj.name
        return form

    def get_grammatical_category(self, obj):
        return obj.grammatical_category.name;

    def get_definitions(self, obj):
      return list((word.definition) for word in
                  sorted(obj.words.all(),
                         key=lambda word: word.definition));

    def get_thematic_categories(self, obj):
        return list((category.name) for category in
                    sorted(obj.thematic_categories.all(),
                           key=lambda category: category.name));

    def get_words(self, obj):
        return list((word.text for word in
                     sorted(obj.words.all(), key=lambda word: word.language)));


admin.site.register(DictionaryEntry, DictionaryEntryAdmin)
admin.site.register(GrammaticalCategory, GrammaticalCategoryAdmin)

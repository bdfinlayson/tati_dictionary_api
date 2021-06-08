from django.contrib import admin

from api.models import EntryEquivalent, DictionaryEntry, GrammaticalCategory

class EntryEquivalentInline(admin.StackedInline):
    model = EntryEquivalent
    min_num = 1
    extra = 0

class GrammaticalCategoryAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)
    search_fields = ('name',)

class DictionaryEntryAdmin(admin.ModelAdmin):
    fields = ('tati_word', 'ipa', 'grammatical_category')
    list_display = ('tati_word', 'ipa', 'entry_equivalents', 'grammatical_category_name', 'definitions',)
    search_fields = ('tati_word', 'ipa', 'entry_equivalents__word', 'grammatical_category__name', 'definitions__text')
    inlines = [EntryEquivalentInline]

    # get_form controls how select options are labeled
    def get_form(self, request, obj=None, **kwargs):
        form = super(DictionaryEntryAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['grammatical_category'].label_from_instance = lambda obj: obj.name
        return form

    def grammatical_category_name(self, obj):
        return obj.grammatical_category.name;

    def definitions(self, obj):
      return list((entry_equivalent.definition) for entry_equivalent in
                  sorted(obj.entry_equivalents.all(),
                         key=lambda entry_equivalent: entry_equivalent.position));

    def thematic_categories(self, obj):
        return list((category.name) for category in
                    sorted(obj.thematic_categories.all(),
                           key=lambda category: category.name));

    def entry_equivalents(self, obj):
        return list((entry_equivalent.word for entry_equivalent in
                     sorted(obj.entry_equivalents.all(), key=lambda entry_equivalent: entry_equivalent.language)));


admin.site.register(DictionaryEntry, DictionaryEntryAdmin)
admin.site.register(GrammaticalCategory, GrammaticalCategoryAdmin)

from rest_framework import serializers
from api.models import DictionaryEntry, EntryEquivalent, GrammaticalCategory


class EntryEquivalentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EntryEquivalent
        fields = ['id', 'language', 'position', 'word', 'definition', 'entry_id']


class GrammaticalCategorySerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = GrammaticalCategory
    fields = ['id', 'name']


class DictionaryEntrySerializer(serializers.HyperlinkedModelSerializer):
    entry_equivalents = EntryEquivalentSerializer(many=True)
    grammatical_category = GrammaticalCategorySerializer(many=False)

    class Meta:
        model = DictionaryEntry
        fields = ['id', 'tati_word', 'ipa', 'createdAt', 'updatedAt', 'grammatical_category', 'entry_equivalents']



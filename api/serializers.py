from rest_framework import serializers
from api.models import DictionaryEntry, EntryEquivalent, GrammaticalCategory


class EntryEquivalentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EntryEquivalent
        fields = ['id', 'language', 'position', 'word', 'definition', 'entry_id']


class DictionaryEntrySerializer(serializers.HyperlinkedModelSerializer):
    entry_equivalents = EntryEquivalentSerializer(many=True)
    class Meta:
        model = DictionaryEntry
        fields = ['id', 'tati_word', 'ipa', 'createdAt', 'updatedAt', 'entry_equivalents']


class GrammaticalCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GrammaticalCategory
        fields = ['id', 'name']


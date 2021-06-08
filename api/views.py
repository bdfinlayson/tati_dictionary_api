from rest_framework import permissions, viewsets
from api.models import DictionaryEntry, EntryEquivalent
from api.serializers import DictionaryEntrySerializer, EntryEquivalentSerializer


class DictionaryEntryViewSet(viewsets.ModelViewSet):
    queryset = DictionaryEntry.objects.all()
    serializer_class = DictionaryEntrySerializer
    permission_classes = [permissions.AllowAny]


class EntryEquivalentViewSet(viewsets.ModelViewSet):
    queryset = EntryEquivalent.objects.all()
    serializer_class = EntryEquivalentSerializer
    permission_classes = [permissions.AllowAny]

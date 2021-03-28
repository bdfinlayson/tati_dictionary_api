from django.core.exceptions import ValidationError
from django.db import models


# summary of data structure of word entry

# Word in Tati
# Word in Persian
# Word in English
# Voice
# IPA
# Grammatical Category
# Thematic category
# Meaning 1
# Meaning 2
# Example (bilingual?)
from django.db.models import DateTimeField

PERSIAN = 0
ENGLISH = 1

LANGUAGE_CHOICES = (
  (PERSIAN, 'Persian'),
  (ENGLISH, 'English')
)

POSITION_CHOICES = (
  (0, 'First'),
  (1, 'Second'),
  (2, 'Third'),
  (3, 'Fourth'),
  (4, 'Fifth')
)


class GrammaticalCategory(models.Model):
    name = models.CharField(max_length=50)


class DictionaryEntry(models.Model):
    tati_word = models.CharField(max_length=100, blank=False, null=False)
    ipa = models.CharField(max_length=150, blank=False, null=False)
    createdAt = DateTimeField(auto_now_add=True)
    updatedAt = DateTimeField(auto_now=True)
    grammatical_category = models.ForeignKey(GrammaticalCategory, related_name="entry", on_delete=models.PROTECT)
    # use clean(self) for validation at save
    #
    # def clean(self):
    #     if len(list(filter(lambda word: word.language == TATI, self.entry_items.all()))) > 1:
    #         raise ValidationError('Only one Tati word per dictionary entry is permitted')


class EntryEquivalent(models.Model):
    language = models.IntegerField(choices=LANGUAGE_CHOICES, default=0)
    position = models.IntegerField(choices=POSITION_CHOICES, default=0)
    word = models.CharField(max_length=250, blank=True, default='')
    definition = models.CharField(max_length=500, blank=True, default='')
    entry = models.ForeignKey(DictionaryEntry, related_name="entry_equivalents", on_delete=models.CASCADE)


class ThematicCategory(models.Model):
    name = models.CharField(max_length=50)
    entries = models.ManyToManyField(DictionaryEntry, related_name="thematic_categories")




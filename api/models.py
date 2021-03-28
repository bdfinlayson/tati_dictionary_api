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

LANGUAGE_CHOICES = (
  (1, 'Tati'),
  (2, 'Persian'),
  (3, 'English')
)

# class Example(models.Model):
#     language = models.IntegerField()
#     position = models.IntegerField()
#     text = models.CharField(max_length=1500)
#

   # examples = models.ManyToManyField(Example)

class GrammaticalCategory(models.Model):
    name = models.CharField(max_length=50)


class DictionaryEntry(models.Model):
    ipa = models.CharField(max_length=250)
    createdAt = DateTimeField(auto_now_add=True)
    updatedAt = DateTimeField(auto_now=True)
    grammatical_category = models.ForeignKey(GrammaticalCategory, related_name="entry", on_delete=models.PROTECT)


class Word(models.Model):
    language = models.IntegerField(choices=LANGUAGE_CHOICES)
    text = models.CharField(max_length=250, blank=True, default='')
    definition = models.CharField(max_length=500, blank=True, default='')
    entry = models.ForeignKey(DictionaryEntry, related_name="words", on_delete=models.CASCADE)


class ThematicCategory(models.Model):
    name = models.CharField(max_length=50)
    entries = models.ManyToManyField(DictionaryEntry, related_name="thematic_categories")




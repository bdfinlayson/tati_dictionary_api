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

LANGUAGE_CHOICES = (
  (1, 'Tati'),
  (2, 'Persian'),
  (3, 'English')
)


class GramaticalCategory(models.Model):
    name = models.CharField(max_length=50)


class ThematicCategory(models.Model):
    name = models.CharField(max_length=50)


# class Example(models.Model):
#     language = models.IntegerField()
#     position = models.IntegerField()
#     text = models.CharField(max_length=1500)
#

   # examples = models.ManyToManyField(Example)


class InternationalPhoneticAlphabet(models.Model):
    text = models.CharField(max_length=250)


class DictionaryEntry(models.Model):
    # grammaticalCategory = models.ForeignKey(GramaticalCategory)
    # thematicCategory = models.ForeignKey(ThematicCategory)
    ipa = models.CharField(max_length=250)


class Word(models.Model):
    language = models.IntegerField(choices=LANGUAGE_CHOICES)
    text = models.CharField(max_length=250)
    entry = models.ForeignKey(DictionaryEntry, on_delete=models.CASCADE)


class Definition(models.Model):
    text = models.CharField(max_length=500)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)



from django.db import models
from model_utils.managers import InheritanceManager
from django.forms import CharField, URLField
from stdimage import StdImageField
from archive.consts import *


class ArchiveDocument(models.Model):
    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.id
    objects = InheritanceManager()
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=False)
    creator = models.CharField(max_length=50, blank="True")
    photo_image = StdImageField(
        upload_to="photographs/",
        variations={"thumbnail": {"width": 300, "height": 300}},
        null=True,
        blank = True,
    )


class AssociatedImage(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    associated_doc = models.ForeignKey(
        ArchiveDocument, blank=False, null=False, on_delete=models.CASCADE)
    creator = models.CharField(max_length=200, blank=True)
    photo_image = StdImageField(
        upload_to="photographs/",
        variations={"thumbnail": {"width": 300, "height": 300}},
        null=False
    )

    def __str__(self):
        return(self.photo_image.url)

class AudioRecording(ArchiveDocument):
    language = models.CharField(max_length=200)
    speaker = models.CharField(max_length=200, blank = True)
    recording_date = models.DateField(auto_now=True)
    audio_file = models.FileField(upload_to="sounds/", null=True)
    
class Photograph(ArchiveDocument):
    photo_type = models.CharField(
        max_length=20,
        choices=list(
            Choices.PHOTO_TYPE_CHOICES.items()
        ),  # defining the constant as a dictionary for easy lookup in views.
    )


class Artifact(ArchiveDocument):
    LEV_EASY = 'Easy'
    LEV_MODERATE = 'Moderate'
    LEV_EXPERIENCED = 'Experienced'
    LEV_DIFFICULT = 'Difficult'
    LEV_EXPERT = 'Expert'


    LEVEL_CHOICES = [(LEV_EASY, "Easy"),
                        (LEV_MODERATE, "Moderate"),
                        (LEV_EXPERIENCED, "Experienced"),
                        (LEV_DIFFICULT, "Difficult"),
                        (LEV_EXPERT,"Expert")]
    level = models.CharField(
        max_length=50, choices=LEVEL_CHOICES, default=LEV_EASY)
    model3d = models.URLField(max_length=500, blank="True")
    country_of_origin = models.TextField(max_length=500, blank = "True")
    physical_description = models.TextField(max_length=10000, blank = "True")
    growth_habits = models.TextField(max_length=10000, blank = "True")
    care_requirements = models.TextField(max_length=10000, blank = "True")
    additional_facts = models.TextField(max_length=10000, blank = "True")


class Document(ArchiveDocument):
    # might want to do something to standardize this later so people can't
    # just enter variant spellings for language names--a preformated list of standard names
    # and codes?
    language = models.CharField(max_length=200)
    transcription = models.TextField(blank=True, null=False)

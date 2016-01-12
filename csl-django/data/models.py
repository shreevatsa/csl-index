from django.db import models

class Volume(models.Model):
    published_year = models.CharField(null=False, blank=False) # Year of publication: not published <=> "No"
    publication_order = models.PositiveSmallIntegerField(null=False, blank=False)
    foreword_by = models.CharField(null=True, blank=True)
    # volume_links =
    categories = models.ManyToManyField(

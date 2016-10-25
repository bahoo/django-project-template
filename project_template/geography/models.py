from django.contrib.gis.db import models
from django.contrib.humanize.templatetags.humanize import ordinal


class AbstractGeography(models.Model):
    title = models.CharField(max_length=255)
    geom = models.MultiPolygonField(blank=True, null=True, srid=4326)
    objects = models.GeoManager()

    def __unicode__(self):
        return self.title

    class Meta:
        abstract = True


class Fips(models.Model):
    fips = models.IntegerField(null=True, blank=True)

    class Meta:
        abstract = True


class State(AbstractGeography, Fips):
    
    class Meta:
        ordering = ('title',)



class BelongsToState(models.Model):
    state = models.ForeignKey(State)

    class Meta:
        abstract = True


class CongressionalDistrict(AbstractGeography, BelongsToState):

    class Meta:
        verbose_name = 'Congressional District'
        ordering = ('title', 'state__title')

    def __unicode__(self):
        return "%s %s, %s" % (ordinal(self.title), self._meta.verbose_name.title(), self.state.title)


class County(AbstractGeography, Fips, BelongsToState):
    
    class Meta:
        verbose_name_plural = 'Counties'
        ordering = ('title', 'state__title')

    def __unicode__(self):
        return "%s %s, %s" % (self.title, self._meta.verbose_name.title(), self.state.title)


class LegislativeDistrict(AbstractGeography, BelongsToState):
    
    class Meta:
        verbose_name = 'Legislative District'
        ordering = ('title',)

    def __unicode__(self):
        return "%s %s, %s" % (ordinal(self.title), self._meta.verbose_name.title(), self.state.title)
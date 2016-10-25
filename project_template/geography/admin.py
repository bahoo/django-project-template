from django.contrib.gis import admin
from .models import *


@admin.register(State)
class StateAdmin(admin.OSMGeoAdmin):
    list_display = ['title']
    
    def get_queryset(self, request):
        return super(StateAdmin, self).get_queryset(request).defer('geom')


@admin.register(CongressionalDistrict)
class CongressionalDistrictAdmin(admin.OSMGeoAdmin):
    list_display = ['title', 'state']
    list_select_related = ['state']
    list_filter = ['state__title']
    
    def get_queryset(self, request):
        return super(CongressionalDistrictAdmin, self).get_queryset(request).select_related('state').defer('geom', 'state__geom')


@admin.register(County)
class CountyAdmin(admin.OSMGeoAdmin):
    list_display = ['title', 'state']
    list_select_related = ['state']
    list_filter = ['state__title']
    
    def get_queryset(self, request):
        return super(CountyAdmin, self).get_queryset(request).select_related('state').defer('geom', 'state__geom')


@admin.register(LegislativeDistrict)
class LegislativeDistrictAdmin(admin.OSMGeoAdmin):
    list_display = ['__unicode__', 'state']
    list_filter = ['state__title']
    
    def get_queryset(self, request):
        return super(LegislativeDistrictAdmin, self).get_queryset(request).select_related('state').defer('geom', 'state__geom')
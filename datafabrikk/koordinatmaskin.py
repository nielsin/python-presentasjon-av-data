# -*- coding: utf-8 -*-

import random
import mgrs
from geopy.geocoders import Nominatim

class RandomCoordinate(object):

    left = -180
    top = 90
    right = 180
    bottom = -90

    m = mgrs.MGRS()
    geolocator = Nominatim(user_agent="geocode_task")

    def __init__(self, bbox=None):

        if bbox is not None:
            self.set_bbox(**bbox)

    def set_bbox(self, left, right, bottom, top):
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom

    def randomCoordinate(self):
        lat = self.bottom + (float(self.top-self.bottom) * random.random())
        lon = self.left + (float(self.right-self.left) * random.random())
        return lon, lat

    def randomMGRS(self):
        lon, lat = self.randomCoordinate()
        return self.m.toMGRS(lat, lon)

    def randomDD(self):
        lon, lat = self.randomCoordinate()
        return '{:.5f}, {:.5f}'.format(lon, lat)

    def randomDMS(self):
        lon, lat = self.randomCoordinate()

        ew = 'E'
        if lon < 0:
            ew = 'W'

        ns = 'N'
        if lat < 0:
            ns = 'S'

        dms_lon = '{:03d}{:02d}{:02d}{}'.format(*[int(c) for c in self.m.ddtodms(lon)], ew)
        dms_lat = '{:02d}{:02d}{:02d}{}'.format(*[int(c) for c in self.m.ddtodms(lat)], ns)

        return '{} {}'.format(dms_lat, dms_lon)

    def randomAddress(self):
        lon, lat = self.randomCoordinate()
        
        location = self.geolocator.reverse((lat, lon), language='NO', addressdetails=True)

        return '{road} {house_number}, {postcode} {city}, {country}'.format(**location.raw['address'])

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Location,Category,Image

class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.remera= Location(location_name="Remera")

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.remera,Location))
    
    # Testing Save Method
    def test_save_location(self):
        self.remera.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def tearDown(self):
        Location.objects.all().delete()
    
    def test_delete_location(self):
        self.remera.delete_location()
        self.assertEqual(len(Location.objects.all()),0)
        

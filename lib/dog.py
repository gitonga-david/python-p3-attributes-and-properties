#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="Fido", breed="Pug"):
        self.name = name
        self.breed = breed
    
    @property
    def name(self):
        return self._name
    
    @name.setter    
    def name(self, value):
        self._name = value if type(value) == str and len(value) > 0 and len(value) < 26 else print("Name must be string between 1 and 25 characters.")

    @property
    def breed(self):
        return self._breed
    
    @breed.setter
    def breed(self, value):
        self._breed = value if value in APPROVED_BREEDS else print("Breed must be in list of approved breeds.")

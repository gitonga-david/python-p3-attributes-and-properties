#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self,name="Test", job="Purchasing"):
        self.name = name
        self.job = job

    @property
    def name(self):
        return  self._name

    @name.setter
    def name(self, value):
        self._name = value.title() if type(value) == str and len(value) > 1 and len(value) < 25 else print("Name must be string between 1 and 25 characters.")
    
    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        self._job = value if value in APPROVED_JOBS else print("Job must be in list of approved jobs.")
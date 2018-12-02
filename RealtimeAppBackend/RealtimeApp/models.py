from django.db import models


# Create your models here
from json import JSONEncoder

class DataModel(JSONEncoder):
    roomLight = False
    benchLight = False
    blender = False
    spaceHeater = False
    roomOccupied = False
    grinder = False

    def __init__(self, roomLight, benchLight, blender, spaceHeater, roomOccupied, grinder):
        self.roomLight = roomLight
        self.benchLight = benchLight
        self.blender = blender
        self.spaceHeater = spaceHeater
        self.roomOccupied = roomOccupied
        self.grinder = grinder
    def __str__(self):
        return "room light: " + str(self.roomLight) + "\n" + \
               "bench light: " + str(self.benchLight) + "\n" + \
               "blender: " + str(self.blender) + "\n" + \
               "space heater: " + str(self.spaceHeater) + "\n" + \
               "room occupied: " + str(self.roomOccupied) + "\n" + \
               "grinder: " + str(self.grinder) + "\n"


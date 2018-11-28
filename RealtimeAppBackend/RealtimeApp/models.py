from django.db import models


# Create your models here
from json import JSONEncoder

class DataModel(JSONEncoder):
    roomLight = False
    benchLight = False
    blender = False
    spaceHeater = False

    def __init__(self, roomLight, benchLight, blender, spaceHeater):
        self.roomLight = roomLight
        self.benchLight = benchLight
        self.blender = blender
        self.spaceHeater = spaceHeater

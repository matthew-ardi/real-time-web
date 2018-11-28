from django.shortcuts import render

# Create your views here.
from rest_framework import *

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from RealtimeApp.models import DataModel
import json

data = DataModel(False, False, False, False)


@api_view(['GET'])
def retrieveData(request):
    # @TODO(matthew-ardi): Please put the code where you receive the data from bluetooth signal here and
    # @TODO:               then modify the global object data
    print("Hello World")
    return Response(json.dumps(data.__dict__), status.HTTP_200_OK)


def setData(data, roomLight, benchLight, blender, spaceHeater):
    data.roomLight = roomLight
    data.benchLight = benchLight
    data.blender = blender
    data.spaceHeater = spaceHeater

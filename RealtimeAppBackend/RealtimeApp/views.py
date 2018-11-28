from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from RealtimeApp.models import DataModel
from django.http import HttpResponse
import pusher
import os
import json

pusher_client = pusher.Pusher(
    app_id='659585',
    key='bb1612a3ac961ac6e2ab',
    secret='8f0e9cffee2c9b2764ae',
    cluster='us2',
    ssl=True
)

data = DataModel(False, False, False, False)


def dashboard(request):
    print(os.getcwd())
    return render(request, "dashboard.html");


@csrf_exempt
def retrieveData(request):
    # @TODO(matthew-ardi): Please put the code where you receive the data from bluetooth signal here and
    # @TODO:               then modify the global object data
    print("Hello World")
    pusher_client.trigger('my-channel', 'my-event', json.dumps(data.__dict__))
    return HttpResponse("done");


def setData(data, roomLight, benchLight, blender, spaceHeater):
    data.roomLight = roomLight
    data.benchLight = benchLight
    data.blender = blender
    data.spaceHeater = spaceHeater

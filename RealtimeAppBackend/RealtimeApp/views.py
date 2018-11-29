from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from RealtimeApp.models import DataModel
from django.http import HttpResponse
import pusher
import os
import json
import time

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

def change(request):
    data.roomLight = not data.roomLight
    data.spaceHeater = not data.spaceHeater
    data.blender = not data.blender
    data.benchLight = not data.benchLight
    return HttpResponse("done");

@csrf_exempt
def retrieveData(request):
    while True:
        pusher_client.trigger('my-channel', 'my-event', json.dumps(data.__dict__))
        time.sleep(3)

@csrf_exempt
def retrieveBluetooth(request):
    # @TODO(matthew-ardi): Please put the code where you receive the data from bluetooth signal here and
    # @TODO:               then modify the global object data
    return



def setData(data, roomLight, benchLight, blender, spaceHeater):
    data.roomLight = roomLight
    data.benchLight = benchLight
    data.blender = blender
    data.spaceHeater = spaceHeater
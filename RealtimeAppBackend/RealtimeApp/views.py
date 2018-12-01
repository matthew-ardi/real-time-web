from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from RealtimeApp.models import DataModel
from django.http import HttpResponse
import pusher
import os
import json
import time
import serial

pusher_client = pusher.Pusher(
    app_id='659585',
    key='bb1612a3ac961ac6e2ab',
    secret='8f0e9cffee2c9b2764ae',
    cluster='us2',
    ssl=True
)

data = DataModel(False, False, False, False, False, False)




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
    # @NOTE(sonminhtran1997): this might not work when running server on your side because it needs our (matthew-ardi) device
    ##
    ##  Getting a set of data through serial communication of the device bluetooth
    ##
    s = serial.Serial('/dev/ttyS0', 115200, timeout=1) 
    string = ""
    final_message = ""
    try:
        while(1):
            c = s.read()    # wait for start character
            if c == '#':
                for i in range (0,7):
                    c = s.readline()
                    string += c
                break
        
        final_message = str(string.split('#', 1)[1])    # String of data transmitted through bluetooth from device
    except:
        return  # sometime exception might happen when server is trying to read serial data but no new data has been sent. 
                # when this happen, skip the process below and let the server re-request serial data.

    ##
    ##  splitting messages to read boolean values of each event detection
    ##
    split_message = final_message.split('\n')
    roomLightState = False
    benchLightState = False
    blenderState = False
    spaceHeaterState = False
    roomOccupiedState = False
    grinderState = False

    event_state = []
    for event in split_message:
        state = event.split(' ')
        if "true" in state:
            event_state.append(True)
        else:
            event_state.append(False)

    roomLightState = event_state[0]
    benchLightState = event_state[1]
    blenderState = event_state[2]
    spaceHeaterState = event_state[3]
    roomOccupiedState = event_state[4]
    grinderState = event_state[5]

    # @TODO:               then modify the global object data
    data(roomLightState, benchLightState, blenderState, spaceHeaterState, roomOccupiedState, grinderState)

    return



def setData(data, roomLight, benchLight, blender, spaceHeater):
    data.roomLight = roomLight
    data.benchLight = benchLight
    data.blender = blender
    data.spaceHeater = spaceHeater

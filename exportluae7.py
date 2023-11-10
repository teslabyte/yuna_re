import time
import frida
import sys
import os
import codecs
import binascii
import base64

def savefile(path, data):
    #Uncomment if hooking loadbuffer
    '''
    if not os.path.exists(os.path.dirname(path)):
        try:
            os.makedirs(os.path.dirname(path))
        except OSError as exc:  # Guard against race condition
            raise
    '''
    with codecs.open(path, 'wb') as f:
        f.write(bytes(data))

def on_message(message, data):
    #print(message)
    if 'payload' in message and message['type'] == 'send':
        payload = message['payload']
        origin_path = payload['path']
        if 'dump' in payload:
            dump = payload['dump']
            savefile(origin_path,dump)
            return
        if message['type'] == 'send':
            print(data)
            savefile(origin_path,data)
        else:
            print(message)

target_process_name = ""
device = frida.get_usb_device()

processes = device.enumerate_processes()
target_process = None

for process in processes:
    if process.name == target_process_name:
        target_process = process
        break

session = device.attach(target_process.pid)
with open("") as f:
    script = session.create_script(f.read())
script.on("message", on_message)
script.load()
sys.stdin.read()
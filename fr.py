import frida
import sys
import msgpack
import lz4.frame

def yuna_xor(buffer, buffer_size, key_index):
    key_size = 256
    key = "Not for Github"

    result = bytearray()

    for byte in buffer:
        v7 = key[key_index % key_size]
        key_index += 1
        result.append(byte ^ v7)
    
    return bytes(result)

def on_message(message, data):
    if 'payload' in message and message['type'] == 'send':
        payload = bytearray(message['payload'])
        key_index = payload[0]
        buffer_array = payload[1:]
        
        dec = yuna_xor(buffer_array, len(buffer_array), key_index)
        test = lz4.frame.decompress(dec)
        print(test.decode("utf-8"))

def on_message_third(message, data):
    if 'payload' in message and message['type'] == 'send':
        payload = message['payload']
        if 'data' in payload:
            data = payload['data']
            key_index = payload['index']

            dec = yuna_xor(data, len(data), key_index)
            print(dec.decode("iso_8859_1"))

target_process_name = "" #Name of the game here
device = frida.get_usb_device()

processes = device.enumerate_processes()
target_process = None

for process in processes:
    if process.name == target_process_name:
        target_process = process
        break

session = device.attach(target_process.pid)
with open("") as f:   #Script location here
    script = session.create_script(f.read())
#script.on("message", on_message_third)
script.load()
sys.stdin.read()
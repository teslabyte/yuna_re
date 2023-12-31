import msgpack
 
def yuna_xor(buffer, buffer_size, key_index):
    key_size = 256
    key = b'Not for github'

    result = bytearray()

    for byte in buffer:
        v7 = key[key_index % key_size]
        key_index += 1
        result.append(byte ^ v7)
    
    return bytes(result)


datas = {
    'data': b'\x9d\xd3\x7c\xaf\xe5\xf8\xd5\xf5\xec\x18\x47\x76\x85\x2b\x80\xcc\xb5\x73\x53\x88\x47\x4a\x2f\xc3\x41\xb3\x12\xc8\x16\xb6\xed\x27\xf6\xfb\xd3\x03\xbc\x9e\x72\xdb\x95\xd4\xd5\x9d\x99\xd2\x16\xd2\xb9\x5f\xdb\x8e\x7c\x27\xe0\x5b\xbd\x90\x63\xfa\xc6\x2d\x5a\x66\xb5\x60\xa1\x5d\x66\x33\x1c\x81\x82\x7c\x40\xbd\xdc\x4e\xda\x50\x3b\xdb\x71\xdc\x30\x92\xff\xba\xf0\x44\xa8\x28\x2c\xe4\x75\xc8\x00\x11\x0f\x9f\xe7\xc7\x2d\xb1\x3b\x3a\x31\x35\xb8\xec\x3b\xe7\x8b\x47\x98\xec\xc9\xb3\xe0\x26\xcd\xc6\x2a\xa4\xb8\x7d\x23\x2d\xca\xb8\x83\x8b\x29\x58\x0b\x56\x30\x24\x49\xba\x61\xf2\x79\x42\x9a\x01\xba\xea\xa9\xb6\x32\x60\x02\xb2\x43\x58\x2c\xfa\x80\x0a\x72\xe9\x77\x0c\xd2\x17\x71\x3d\xef\x12\x84\x63\x0d\x76\x07\xc6\x75\xd4\xf6\xe3\xeb\x40\x8e\x24\xca\xd0\xb0\xa6\x64\xcc\x46\x77\x9a\x09\x10\x21\xcf\x4c\x7f\xe3\x99\x2c\x91\xf9\x10\x87\x9b\x73\xab\xf7\x03\x92\x87\xd7\x09\x1d\xa5\x9b\x14\x57\x13\xf8\x34\x78\x7d\xac\x6e\xa8\xfc\x78\xf9\xb2\xde\x81\x3d\x2d\xf2\x07\x60\xf9\x2a\xd3\x08\x01\xf3\xab\xb8\x7c\x75\x9c\xaa\x33\xa8\x50\xe7\x19\x74\x1d\x7d\x9a\xf0\x60\x1e\xef\xe7\xc6\x47\x7d\xb8\x20\x9d\x3b\xb7\x6c\x45\x85\x57\x70\xec\xc6\x8d\xb2\x16\xd7\x13\x5d\x3a\x27\xf5\xfd\xc0\x18\x1c\xf0\xd0\xbe\xbd\xef\x26\x25\x2d\xbf\x2c\xa4\x48\x25\x49\xcd\x7b\x63\xe6\x04\xda\xcc\x3b\xa9\xcd\xf6\x53\x62\xe0\x35\xa3\x0b\x69\x35\x48\xd0\x8a\x7c\x40\xbd\xd1\xd9\x81\x10\x69\x82\x35\xac\xa2\xcf\xf2\x74\xe4\x58\x85\x38\x2a\xfe\x75\xe3\x69\xd5\x0d\x95\x5e\xae\x4e\xd4\x74\x75\x2d\x7a\x79\x48\x6b\xb4\x9b\x4c\x1c\xf4\xce\xf3\xeb\x6d\xc2\x9a\x7c\xf5\xf9\x14\x66\x3f\x99\xed\x91\xde\xe9\x0d\x51\x0b\x3a\x7d\x19\x05\x56\xef\x4b\xb1\xa8\x36\x9a\xdc\x93\x8a\x15\x87\x2e\xbf\x16\x5d\x27\xe8\xd7\x56\xb1\xfe\x61\x0f\x89\x52\x9f\x0e\x91\x4c\x89\x3b\x0f\x77\x53\xcd\x72\xd6\xf7\xe0\xb4\x46\x8c\x27\x9d\x81'    
}

for key, value in datas.items():
    key_index = value[0]

    #print(key_index)
    data = value[1:]

    result = yuna_xor(data, len(data), key_index)
    print(len(result))
    result_decoded = msgpack.unpackb(result[3:], raw=False)
    unknown = result[:3]
    print(result_decoded)



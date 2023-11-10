from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


cbc_key = "not putting this on github"

def aes_cbc(encrypted_text):
    decoded = b64decode(encrypted_text)

    iv = decoded[:16]
    to_dec = decoded[16:]

    cipher = AES.new(cbc_key, AES.MODE_CBC, iv = iv)

    decrypted_data = cipher.decrypt(to_dec)
    
    unpadded_data = unpad(decrypted_data, AES.block_size)
    return unpadded_data.decode("utf-8")


data = "u/FL2kRm8BtxupfHLYRx0nNgnmVzs2HPrdR9TAe8EG0="

result = aes_cbc(data)
print(result)


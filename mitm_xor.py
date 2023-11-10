import os
import math
import random

def calculate_lbnum():
    qword = b'\xff\xff\xff\xff\xff\xff\xff\xff'

    # Specify the file path
    file_path = ""  

    # Check if the file exists
    if os.path.exists(file_path):
        # Get the size of the file in bytes
        file_size = os.path.getsize(file_path)
        print(f"The file size is {file_size} bytes")

        result = int.from_bytes(qword) ^ (32 * file_size + 32845)  # Cpp magic
        print(result)
    else:
        print("File does not exist.")


def var_45_4(a, b):
    v46 = 0
    for i in range(32):
        middle = a/2 + b/2

        if middle != math.floor(middle):
            v46 += 2**i

        a = math.floor(a/2)
        b = math.floor(b/2)

    return v46


def var_45_5(func_arg):
    func_arg = str(func_arg)

    while len(func_arg) < 255:
        func_arg += chr(random.randint(48,90))


    random_int = random.randint(0, 255)
    num_array = [
		222,
		160,
		133,
		144,
		196,
		175,
		184,
		122,
		35,
		110,
		57,
		222,
		216,
		113,
		163,
		212,
		51,
		57,
		209,
		76,
		169,
		254,
		129,
		252,
		190,
		81,
		181,
		238,
		141,
		185,
		90,
		192,
		184,
		164,
		7,
		221,
		64,
		235,
		220,
		146,
		235,
		134,
		219,
		137,
		123,
		238,
		58,
		47,
		206,
		203,
		186,
		35,
		29,
		112,
		251,
		252,
		141,
		232,
		187,
		142,
		165,
		242,
		107,
		68
    ]

    empty_array = []

    num_array_len = len(num_array)
    formatted = format(random_int, '02x')

    for char in func_arg:
        formatted += format(var_45_4(ord(char),num_array[(random_int + 1) % num_array_len]), '02x')

    return formatted


rand_chars = '9z|ym9}ovp9wkz}'
proc_self_maps = ''

for i in range(1, len(rand_chars)):
    proc_self_maps += chr(ord(rand_chars[i]) - 10)

print(proc_self_maps)


res = var_45_5('b0m3mqdo')
print(res)



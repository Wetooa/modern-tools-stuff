from random import randint, random

print("RandINT qGen Yea")
q = 5
for _ in range(q):
    n = randint(0, 128)
    print("N: " + str(n))

    print("bin: " + bin(n).replace('0b', ''))
    print("oct: " + oct(n).replace('0o', ''))
    print("hex: " + hex(n).replace('0x', ''))
    print("--------")

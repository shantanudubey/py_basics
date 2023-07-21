# Binary Numbers and their workings.

print('-' * 80)
a = b'\x00\x01\x01\x81'
print("Binary           :", a)
n1 = int.from_bytes(a, "big")
n2 = int.from_bytes(a, "little")
print("int from bytes   :", n1, n2)

print('-' * 80)


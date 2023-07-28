import json

print('-'*79)
# Serializing/Deserializing user-defined types
# We create a new type called "Complex"
print("Serializing User Defined objects.")
class Complex:
    def __init__(self, r=0, i=0) -> None:
        self.real = r
        self.imag = i

    def print_data(self):
        print(self.real, self.imag)

def encode_complex(x):
    if isinstance(x, Complex):
        return {'real':x.real, 'imag':x.imag}
    else:
        raise TypeError("Complex object isn't Serializable.")

def decode_complex(dct):
    # Using attribute signatures to find the class
    if "__Complex__" in dct:
        return Complex(dct['real'], dct['imag'])
    return dct

c = Complex(1.0, 2.0)
c.print_data()

with open("data", "w+") as f:
    json.dump(c, f, default=encode_complex)
    f.seek(0)
    inc = json.load(f, object_hook=decode_complex)
    print(type(inc), inc)
    f.close()

# TODO check 
print("XXXX :", dir(c))
print("XXXX :", vars(c))



print('-'*79)
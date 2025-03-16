"""
Extended Euclidean For Polynomial

Akhmad Sultoni
17 Maret 2025
"""

"""
Instal terlebih dahulu galois:
    pip install galois
"""


import galois
GF=galois.GF(2**8,irreducible_poly=galois.Poly([1, 0, 0, 0, 1, 1, 0, 1, 1],field=galois.GF(2)))

GF.repr("poly")

x=input('Masukan nilai hexadecimal: ')

a=int(x,16)

polinomial=GF(a)
bit_representation = bin(int(polinomial))[2:].zfill(8)
invers=polinomial**(-1)
bit_invers=bin(int(invers))[2:].zfill(8)
print(f'Bentuk Byte dari hexadecimal {x}: ', bit_representation)
print(f'Bentuk polinomial dari hexadecimal {x}: ',polinomial)

print('\nPolinomial Invers: ',invers)
print('Bentuk byte dari inversnya: ',bit_invers)

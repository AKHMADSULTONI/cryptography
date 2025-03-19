# -*- coding: utf-8 -*-
"""
Transformasi SubBytes() dalam AES

Akhmad Sultoni
19 Maret 2025
"""


import galois
GF=galois.GF(2**8,irreducible_poly=galois.Poly([1, 0, 0, 0, 1, 1, 0, 1, 1],field=galois.GF(2)))
GF.repr("poly")

# Fungsi SubBytes()
def SubBytes(hex_angka):
    bit_p=[0,1,1,0,0,0,1,1]
    c=bit_p[::-1]
    polinomial=GF(a)
    bit_pol = bin(int(polinomial))[2:].zfill(8)
    bit_poli=bit_pol[::-1]
    invers=polinomial**(-1)
    bit_inv=bin(int(invers))[2:].zfill(8)
    bit_invers=bit_inv[::-1]
    b=[]
    for i in range(8):
        bb=0
        bb=int(c[i])+int(bit_invers[i])+int(bit_invers[((i+4)%8)])+int(bit_invers[((i+5)%8)])+int(bit_invers[((i+6)%8)])+int(bit_invers[((i+7)%8)])
        kk=0
        kk=bb%2
        b.append(kk)
    balik=b[::-1]
    return balik, polinomial, invers

# Fungsi merubah binary ke List Hexadecimal
def binary_list_to_hex(binary_list):
  binary_string = "".join(map(str, binary_list))
  decimal_value = int(binary_string, 2)
  hexadecimal_string = hex(decimal_value)[2:]  # Remove "0x" prefix
  return hexadecimal_string

#Input kata yang akan dienkripsikan 
plaintext=input('masukan kata tanpa spasi dengan huruf kecil: ')
print('\nAkan dilakukan Transformasi SubBytes()')

hex_angka = ""
for k in plaintext:
    hex_angka= hex(ord(k))[2:]
    x=hex_angka
    a=int(x,16)
    hasil, pol, inv=SubBytes(a)
    binary_list = hasil
    hexadecimal_value = binary_list_to_hex(binary_list)
    print(f'\nBentuk Hexadecimal Plaintext {k}: ',x)
    print(f'Bentuk Polinomial dari Hexadecimal Plaintext {hex_angka}: ',pol)
    print('Invers Polinomialnya: ',inv)
    print(f"Hasil SubBytes {hex_angka} adalah ",hexadecimal_value)

# -*- coding: utf-8 -*-
"""
Fungsi AddRoundKey()

Akhmad Sultoni
23 Maret 2025
"""

import numpy as np

# Fungsi merubah plaintex menjadi hexadecimal
def rubah(isi):
    temp=""
    for k in isi:
        hexa=hex(ord(k))[2:]
        temp+=hexa
    return temp

# Fungsi merubah bentuk ke matrik state
def state(isi):
    temp=[]
    if len(isi) < 32:
        kosong=32-len(isi)
        isi+="0"*kosong
    temp2 = []
    for i in range(0,32,2):
        hex_2 = isi[i:i+2]
        temp2.append(hex_2)
    hasil=np.array(temp2).reshape(4,4).T
    return hasil

# Fungsi merubah bentuk array ke kalimat
def matriks_ke_kalimat(matriks):
    kalimat = ""
    for baris in matriks:
        for elemen in baris:
            kalimat += str(elemen)
    return kalimat.strip()
    
# Fungsi merubah hexadecimal menjadi biner
def hex_to_bin(hex_string):
    scale = 16 ## equals to hexadecimal
    num_of_bits = 4
    return bin(int(hex_string, scale))[2:].zfill(len(hex_string) * num_of_bits)

# Fungsi merubah biner menjadi hexadecimal
def bin_to_hex(binary_list):
    scale = 16 ## equals to hexadecimal
    num_of_bits = 8
    hex_value = hex(int(binary_list, 2))[2:].zfill(2)
    return hex_value

# Fungsi melakukan xor
def xor(isi,isi1):
    isi1=hex_to_bin(isi1)
    isi=hex_to_bin(isi)
    result=""
    for i in range(len(isi)):
        if isi[i]==isi1[i]:
            result+="0"
        else:
            result+="1"
    result=bin_to_hex(result)
    return result

# Contoh
plaintext="00112233445566778899aabbccddeeff"
key="000102030405060708090a0b0c0d0e0f"

# Merubah hexadecimal ke bentuk matriks
st=state(plaintext)
ky=state(key)

# Perhitungan AddRoundKey()
addR=[]
for i in range(4):
    for j in range(4):
        # print(st[j][i])
        # print(ky[j][i])
        hasil2=xor(st[j][i],ky[j][i])
        addR.append(hasil2)
addR=np.array(addR).reshape(4,4).T
rounde=matriks_ke_kalimat(addR.T)
print(addR)
print('\nRound 1 Start: ',rounde)
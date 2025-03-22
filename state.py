# -*- coding: utf-8 -*-
"""
Membuat State dari Plaintext

Akhmad Sultoni
22 Maret 2025
"""

import numpy as np

# Fungsi untuk merubah ke bentuk hexadecimal
def rubah(isi):
    temp=[]
    for k in isi:
        hexa=hex(ord(k))[2:]
        temp.append(hexa)
    if len(temp)<16:
        kosong=16-len(temp)
        temp.extend([0]*kosong)
    hasil=np.array(temp).reshape(4, 4).T
    return hasil


plaintext=input('Masukan Plaintext: ')

state=rubah(plaintext)
print('\nState: \n',state)




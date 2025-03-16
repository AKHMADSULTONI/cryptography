'''
KODING PYTHON UNTUK CRYPTOSYSTEM 2.6. PERMUTATION CIPHER

Akhmad Sultoni
23/528781/PPA/06688
'''

import numpy as np
import math

#Bagian Pemetaan Enkripsi
def eK(plaintext,key):
    n=len(key) # Panjang kunci
    k=len(plaintext) # Panjang Plaintext
    jumlah_blok=math.ceil(k/n) # jumlah blok yang terbentuk

    chipertext=''
    for i in range(jumlah_blok):
        blok=plaintext[i*n:(i+1)*n]
        permutasi_blok=""
        for j in range(n):
            if i*n+j<len(plaintext):
                permutasi_blok+=blok[key[j]-1]
        chipertext+=permutasi_blok
    return chipertext

#Bagian Pemetaan Dekripsi
def dK(ciphertext,invers):
    n=len(invers) # Panjang kunci
    k=len(ciphertext) # Panjang Plaintext
    jumlah_blok=math.ceil(k/n) # jumlah blok yang terbentuk
    
    hasil=""
    for i in range(jumlah_blok):
        blok=ciphertext[i*n:(i+1)*n]
        hasil_permutasi=""
        for j in range(n):
            if i*n+j<len(plaintext):
                hasil_permutasi+=blok[invers[j]-1]
        hasil+=hasil_permutasi
    return hasil

def Key(key1):
    key=[]
    for i in range(len(key1)):
      k=key1[i]
      key.append(int(k))
    return key

def inv(key):
    invers=[]
    for i in range(len(key)):
      inv=key.index(i+1)+1
      invers.append(inv)
    return invers

# Input kata
plaintext=input('Masukan kata: ')

print('\nTEKS INI AKAN DI ENKRIPSI DENGAN PERMUTATION CIPHER')

# Input Kunci
key1=input('Masukan kunci permutasi:')

print('Plaintext: ',plaintext)
k=len(plaintext)
key=Key(key1) # merubah input berupa string menjadi list numerik
# Menambahkan '0' pada plainteks yang mod(kunci) tidak = 0
while len(plaintext)%len(key)!=0:
    plaintext+='0'

# Proses Enkripsi
ciphertext=eK(plaintext,key)
print('Chipertext: ',ciphertext)

#Invers key
invers=inv(key)

print('Kunci: ',key,'\nInvers Kunci: ',invers)

#Dekripsi
hasil=dK(ciphertext,invers)
kk=len(hasil)-k
hasil=hasil[:-kk]
print('Dekripsi: ',hasil)

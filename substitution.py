'''
KODING PYTHON UNTUK CRYPTOSYSTEM 2.2. SUBSTITUTION CIPHER

Akhmad Sultoni
23/528781/PPA/06688
'''

#Bagian Pemetaan Enkripsi Substitution Ciper
def eK(x):
    return kunci[x]

#Bagian Pemetaan Dekripsi Substitution Ciper
def dK(y):
    k=kunci.index(y)+97
    k1=chr(k)
    return k1

#Input teks yang akan dienkripsi
plaintext=input('masukan kata tanpa spasi dengan huruf kecil: ')
print('\nTEKS TERSEBUT AKAN DIENKRIPSI MENGGUNAKAN SUBSTITUTION CIPHER')
#Input kunci permutasi abjad dengan menggunakan huruf kapital
kunci=input('masukan kunci permutasi abjad:')

#Proses Enkripsi
K=[]
D=[]
for k in plaintext:
    kata=ord(k)-ord('a')
    y=eK(kata)
    K.append(y)
ciphertext=''.join(K)
print('\nciphertext:',ciphertext)

#Proses Dekripsi
for k in ciphertext:
    d=dK(k)
    D.append(d)
dekripsi=''.join(D)
print('dekripsi:',dekripsi)
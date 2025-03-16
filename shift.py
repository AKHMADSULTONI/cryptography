'''
KODING PYTHON UNTUK CRYPTOSYSTEM 2.1. SHIFT CIPHER

Akhmad Sultoni
23/528781/PPA/06688
'''

#Bagian Pemetaan Enkripsi Shift Ciper
def eK(x,K):
    y=(x+K)%26
    return y

#Bagian Pemetaan Dekripsi Shift Ciper
def dK(y,K):
    return (y-K)%26

#Input kata yang akan dienkripsikan dan jarak/shift sejauh K
plaintext=input('masukan kata tanpa spasi dengan huruf kecil: ')
print('\nTEKS INI AKAN DI ENKRIPSI DENGAN SHIFT CIPHER')
K=int(input('Masukan pergeseran sejauh K: '))
T=[]
Z=[]
for k in plaintext:
    x=ord(k)-ord("a")
    y1=eK(x,K)
    y=chr(y1+ord("A"))
    T.append(y)
cipertext=''.join(T)
for k in T:
    y=ord(k)-ord("A")
    x1=dK(y,K)
    x=chr(x1+ord('a'))
    Z.append(x)
dekripsi=''.join(Z)
print('\nCipertext:',cipertext)
print('Hasil Dekripsi:',dekripsi)
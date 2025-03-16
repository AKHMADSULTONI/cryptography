'''
KODING PYTHON UNTUK CRYPTOSYSTEM 2.4. VIGENERE CIPHER

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
print('\nTEKS INI AKAN DI ENKRIPSI DENGAN VIGENERE CIPHER')
m=int(input('\nInput banyaknya m: '))
K=[]
for i in range(m): 
    K1=int(input('Masukan pergeseran sejauh K:'))
    K.append(K1)
T=[]
Z=[]
z=0
for k in plaintext:
    h=z%m
    x=ord(k)-ord("a")
    y1=eK(x,K[h])
    y=chr(y1+ord("A"))
    T.append(y)
    z+=1
cipertext=''.join(T)
l=0
for k in T:
    h1=l%m
    y=ord(k)-ord("A")
    x1=dK(y,K[h1])
    x=chr(x1+ord('a'))
    Z.append(x)
    l+=1
dekripsi=''.join(Z)
print('\nCipertext:',cipertext)
print('Hasil Dekripsi:',dekripsi)
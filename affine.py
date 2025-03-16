'''
KODING PYTHON UNTUK CRYPTOSYSTEM 2.1. Affine CIPHER

Akhmad Sultoni
23/528781/PPA/06688
'''

def eK(x,a,b):
    return (a*x+b)%26

def dK(y,ia,b):
    return ia*(y-b)%26

def fpb(a, c=26):
    while c != 0:
        a, c = c, a % c
    return a
def invers(a):
    k=0
    while (a*k)%26 !=1:
        k+=1
    return k

#Input kata yang akan dienkripsikan dan affine
plaintext=input('masukan kata tanpa spasi dengan huruf kecil: ')
print('\nTEKS INI AKAN DI ENKRIPSI DENGAN SHIFT CIPHER')
a=int(input('Masukan nilai a: '))
b=int(input('Masukan nilai b: '))
T=[]
Z=[]
if fpb(a,26)==1:
    for k in plaintext:
        x=ord(k)-ord("a")
        y1=eK(x,a,b)
        y=chr(y1+ord("A"))
        T.append(y)
    cipertext=''.join(T)
    print('\nCipertext:',cipertext)
    ia=invers(a)
    for k in T:
        y=ord(k)-ord("A")
        x1=dK(y,ia,b)
        x=chr(x1+ord('a'))
        Z.append(x)
    dekripsi=''.join(Z)
    print('Hasil Dekripsi:',dekripsi)

else:
    print(f'\nfpb({a},26) tidak sama dengan 1')


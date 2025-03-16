"""
Program mencari nilai GCD

Akhmad Sultoni
16 Maret 2025
"""
import math
a=int(input('Masukan Nilai a: '))
b=int(input('Masukan Nilai b: '))

r=[]
r.append(a)
r.append(b)
m=1
q=[]
while r[m] != 0:
    q.append(math.floor(r[m-1]/r[m]))
    r.append(r[m-1]-q[m-1]*r[m]) 
    m+=1
m=m-1
print(f'gcd({a},{b}) adalah: ',r[m])
"""
Multiplicative Inverse (a,b)

Akhmad Sultoni
16 Maret 2025
"""

import math

a=int(input("Masukan Nilai a: "))
b=int(input("Masukan Nilai b: "))

a0=a
b0=b
t0=0
t=1
q=math.floor(a0/b0)
r=a0-q*b0
while r>0:
    temp=(t0-q*t)% a
    t0=t
    t=temp
    a0=b0
    b0=r
    q=math.floor(a0/b0)
    r=a0-q*b0
if b0 !=1:
    print(f"b={b} tidak mempunyai invers modulo a={a}")
else:
    print(f'invers b={b} adalah {t}')
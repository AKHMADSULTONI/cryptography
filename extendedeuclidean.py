"""
EXTENDED EUCLIDEAN ALGORITHM

Akhmad Sultoni
16 Maret 2025
"""

import math

a=int(input('Masukan nilai a: '))
b=int(input('Masukan nilai b: '))

a0=a
b0=b
t0=0
t=1
s0=1
s=0
q=math.floor(a0/b0)
r=a0-q*b0

while r>0:
    temp=t0-q*t
    t0=t
    t=temp
    temp=s0-q*s
    s0=s
    s=temp
    a0=b0
    b0=r
    q=math.floor(a0/b0)
    r=a0-q*b0
r=b0
print(f'{r}=gcd({a},{b}), dan {s}x{a}+{t}x{b}={r}')

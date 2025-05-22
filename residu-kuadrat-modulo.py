# -*- coding: utf-8 -*-
"""
Residu Kuadrat Modulo

Akhmad Sultoni
22 Mei 2025
"""
import numpy as np

p=int(input('Masukan bilangan prima >2: '))

for a in range(p):
    if a**((p-1)/2)%p ==1:
        print(f'{a} adalah Residu kuadrat Modulo {p}')
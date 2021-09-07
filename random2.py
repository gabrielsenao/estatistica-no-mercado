#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 13:02:41 2021

@author: gabriel
Gerar Numeros aleatorios Funcao RANDOM
"""
import matplotlib.pyplot as fig
import random

alea=[]
for i in range(100):
    x=random.uniform(-1,+1)
    alea.append(x)
fig.plot(alea,color='black')
fig.xlabel('eixo horizontal')
fig.ylabel('numeros aleatorios entre 0 e 1')

#cria-se uma lista vazia "alea" e usando o for usamos "random" para gerar
#numeros aleatorios entre 0 e 1
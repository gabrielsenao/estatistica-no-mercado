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
for i in range(1000):
    x=random.gauss(0,1)
    alea.append(x)
fig.subplot(211)
fig.plot(alea,color='black')
fig.xlabel('eixo horizontal')
fig.ylabel('numeros aleatorios entre -1 e 1')

fig.subplot(212)
fig.plot(alea,color='grey')
fig.xlabel('classes')
fig.ylabel('frequencia')



#cria-se uma lista vazia "alea" e usando o for usamos "random" para gerar 1000
#numeros aleatorios entre 0 e 1
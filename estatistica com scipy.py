#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 12:12:08 2021

@author: gabriel
Estatistica com Scipy
"""
import xlrd
import statistics as st
import matplotlib.pyplot as fig
import math

wb=xlrd.open_workbook('EstatDad.xls')
p=wb.sheet_by_name('Planilha1')

linha=p.nrows
coluna=p.ncols

dados=[]

for i in range(coluna):
        coluna=p.col_values(i)
        dados.append(coluna)
        print(coluna)
        
retorno=[]

for i in range(linha-2):
        x=(dados[1][i+1]-dados[1][i])/dados[1][i]
        retorno.append(coluna)
        print(x)

fig.figure()
fig.plot(retorno)

fig.figure()
fig.hist(retorno,bins=5, density=True)

fig.figure()
fig.boxplot(retorno)

minimo=min(retorno)
maximo=max(retorno)
media=st.mean(retorno)
mediana=st.median(retorno)
desvp=st.pstdev(retorno)

otimista=media+2*desvp/math.sqrt(linha-2)
pessimista=media-2*desvp/math.sqrt(linha-2)
print("++++++ Estatisticas +++++")
print("Maximo= ",maximo)
print("Minimo= ",minimo)
print("Media= ",media)
print("Mediana= ",mediana)
print("Desvio Padrao= ",desvp)
print("IC = [",pessimista," , ",otimista,"]")












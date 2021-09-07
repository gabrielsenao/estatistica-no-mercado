#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 20:20:50 2021

@author: gabriel
"""
import pandas as pd
import xlrd 
import matplotlib.pyplot as fig
import statistics as st
wb=xlrd.open_workbook('EstatDad.xls')
p=wb.sheet_by_name('Planilha1')

col=p.ncols
lin=p.nrows
    

dados=[]

for i in range(col):
    coluna=p.col_values(i)
    dados.append(coluna)
    
media=st.mean(dados[1][:])
mediana=st.median(dados[1][:])
desvpadP=st.pstdev(dados[1][:]) #desvio padrao populacional
desvpadA=st.stdev(dados[1][:]) #desvio padrao amostral

print('++++++++ Resumo das Estatisticas +++++++')
print('Media Mediana Dsv.P Dsv.A')
print('%5.2f %6.2f %5.2f %5.2f' % (media, mediana, desvpadP, desvpadA))
            
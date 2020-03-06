# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 15:33:04 2020

@author: renatons
"""

#%%
import pandas as pd
import numpy as np
import os
from collections import Counter
from tqdm import tqdm

#%%

dir_inicial = os.getcwd()
os.chdir(r'C:\Users\RenatoNS\Desktop\workspace\agrupamento_BF\bases_de_dados')

df_entrada = pd.read_csv('201901_BolsaFamilia_Pagamentos.csv', sep=';', encoding='latin1' )

df_saida = pd.read_csv('base_saida_testes.csv', sep=';', nrows=100000)

#%% Converte os valores para float

df_entrada['VALOR PARCELA'] = df_entrada['VALOR PARCELA'].apply(lambda x: x.replace(',', '.')).astype(float)

df_saida['VALOR PARCELA'] = df_saida['VALOR PARCELA'].apply(lambda x: x.replace(',', '.')).astype(float)

#%% Soma os valores recebidos por estado: 

uf_list = list(Counter(df_entrada['UF']).keys())

uf_dict = {i : 0 for i in uf_list}

for uf in tqdm(uf_list): 
  uf_dict[uf] = df_entrada['VALOR PARCELA'][df_entrada['UF'] == uf].sum()

'''
for uf in tqdm(uf_list): 
  for uf_index, uf_nome in enumerate(tqdm(df_entrada['UF'])):
    if str(df_entrada.loc[uf_index, 'UF']) == uf:
      uf_dict[uf] += df_entrada.loc[uf_index, 'VALOR PARCELA']
'''

#%% Soma os valores recebidos por município:

municipios_list = list(Counter(df_entrada['NOME MUNICÍPIO']).keys())

municipios_dict = {i : 0 for i in municipios_list}

for municipio in tqdm(municipios_list): 
  municipios_dict[municipio] = df_entrada['VALOR PARCELA'][df_entrada['NOME MUNICÍPIO'] == municipio].sum()

'''
for municipio in tqdm(municipios_list): 
  for municipio_index, municipio_nome in enumerate(df_entrada['NOME MUNICÍPIO']):
    if str(df_entrada.loc[municipio_index, 'NOME MUNICÍPIO']) == municipio:
      municipios_dict[municipio] += df_entrada.loc[municipio_index, 'VALOR PARCELA']
'''
      
#%% Caso o usuário saque menos do que o valor total:
      
for user_index, user in enumerate(tqdm(df_entrada['NIS FAVORECIDO'])):
  if df_entrada.loc[user_index, 'NIS FAVORECIDO'] == df_saida[user_index, 'NIS FAVORECIDO']:
    if df_saida['NIS FAVORECIDO'] < df_entrada['NIS FAVORECIDO']:
      print(df_saida['NIS FAVORECIDO'])


    
#%%

uf_list = list(Counter(df_entrada['UF']).keys())
uf_dict = {i : 0 for i in uf_list}


df = df_entrada.pivot_table(index='UF',columns='VALOR PARCELA',aggfunc=sum)
df = df_entrada

pd.pivot_table(df, index=['UF'], values=['VALOR PARCELA'], aggfunc=np.mean)


for uf in tqdm(uf_list): 
  for uf_index, uf_nome in enumerate(tqdm(df_entrada['UF'])):
    if str(df_entrada.loc[uf_index, 'UF']) == uf:
      uf_dict[uf] += df_entrada.loc[uf_index, 'VALOR PARCELA']



#%%      
df_comparado 

df_steste
      
      
#%%

#df_soma['Total'] = df_soma[]

cont = Counter(df_soma['UF'])

cont.keys()
cont.values()

estados = list(cont.keys())


#%%
'''
import pandas as pd

df = pd.DataFrame(columns = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro', 'Dezembro'])

df = df.set_axis(range(1,13), axis='columns', inplace=False)

# Exemplo
df = df.drop(['Abril'],axis=1)

df.loc['linha', 'coluna'] + df.loc['linha', 'coluna']
'''

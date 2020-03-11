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
def descobre_arquivos_na_pasta(pasta, tipo_do_arquivo='.xlsx'):
    arquivos = []
    for file in os.listdir(pasta):
        arquivos.append(os.fsdecode(file))
    arquivos = [arquivo for arquivo in arquivos if tipo_do_arquivo in arquivo]
    return arquivos


def carregar_tratar_base(nome_arquivo):
  df = pd.read_csv(nome_arquivo, sep=';', encoding='latin1' )
  df['VALOR PARCELA'] = df['VALOR PARCELA'].apply(lambda x: x.replace(',', '.')).astype(float)
  return df


def dict_list_mes_uf(df):
  uf_list = list(Counter(df['UF']).keys())
  uf_dict = {i : 0 for i in uf_list}
  return uf_list, uf_dict


def soma_uf(df):
  for uf in tqdm(uf_list):
    uf_dict[uf] = df['VALOR PARCELA'][df['UF'] == uf].sum()
  for uf in tqdm(uf_dict):
    uf_dict[uf] = str(uf_dict[uf])
  return uf_dict


def dict_list_mes_municipios(df):
  municipios_list = list(Counter(df['NOME MUNICÍPIO']).keys())
  municipios_dict = {i : 0 for i in municipios_list}
  return municipios_list, municipios_dict


def soma_municipios(df):
  for municipio in tqdm(municipios_list):
    municipios_dict[municipio] = df['VALOR PARCELA'][df['NOME MUNICÍPIO'] == municipio].sum()
  for municipio in tqdm(municipios_dict):
    municipios_dict[municipio] = str(municipios_dict[municipio])
  return municipios_dict

#%%
dir_inicial = os.getcwd()
os.chdir(r'C:\Users\RenatoNS\Desktop\workspace\agrupamento_BF\bases_de_dados')
pasta = r'C:\Users\RenatoNS\Desktop\workspace\agrupamento_BF\bases_de_dados'


#%%
meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho",
         "agosto", "setembro", "outubro", "novembro", "dezembro"]

dict_var = {"janeiro":"01", "fevereiro":"02", "março":"03", "abril":"04",
         "maio":"05", "junho":"06", "julho":"07", "agosto":"08", "setembro":"09",
         "outubro":"10", "novembro":"11", "dezembro":"12"}

arquivos = descobre_arquivos_na_pasta(pasta, tipo_do_arquivo='.csv')

#%% Execução por UF
for mes, i in enumerate(meses):
  df = carregar_tratar_base(arquivos[mes])
  uf_list, uf_dict = dict_list_mes_uf(df)
  uf_dict = soma_uf(df)
  dict_var[meses[mes]] = pd.DataFrame.from_dict(uf_dict, orient='index', columns= [meses[mes]]).sort_index(axis = 0)

df = pd.DataFrame()
for mes in dict_var:
  df[mes] = dict_var[mes][mes]
  
# Salva o df por uf em .csv
df.to_csv('total_por_uf.csv',sep=';', encoding="utf-8-sig")


#%% Execução por municípios
for mes, i in enumerate(meses):
  df = carregar_tratar_base(arquivos[mes])
  municipios_list, municipios_dict = dict_list_mes_municipios(df)
  municipios_dict = soma_municipios(df)
  dict_var[meses[mes]] = pd.DataFrame.from_dict(municipios_dict, orient='index', columns= [meses[mes]]).sort_index(axis = 0)

for mes in dict_var:
  df[mes] = dict_var[mes][mes]

# Salva o df por municipios em .csv
df.to_csv('total_por_municipios.csv',sep=';', encoding="utf-8-sig")


#%%

df = dict_var['janeiro']
df['fevereiro'] = dict_var['fevereiro']['fevereiro']


df = pd.DataFrame()

  
list_var_name_uf = []

for i in range(12):
  list_var_name_uf[i] = 'uf_dict_'+list_meses[i]



dict_meses['janeiro'] = carregar_tratar_base(arquivos[0])

dict_meses = {"janeiro":"0", "fevereiro":"0", "março":"0", "abril":"0", "maio":"0",
         "junho":"0", "julho":"0", "agosto":"0", "setembro":"0", "outubro":"0",
         "novembro":"0", "dezembro":"0"}

list_meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", 
              "agosto", "setembro", "outubro", "novembro", "dezembro"]



for uf in tqdm(uf_list): 
  uf_dict_fevereiro[uf] = df_entrada_fevereiro['VALOR PARCELA'][df_entrada_fevereiro['UF'] == uf].sum()

for uf in uf_dict_fevereiro:
  uf_dict_fevereiro[uf] = str(uf_dict_fevereiro[uf])

df_soma_fevereiro = pd.DataFrame.from_dict(uf_dict_fevereiro, orient='index', columns=['Total_Fevereiro'])

df_soma_fevereiro.columns = ['Total_Fevereiro']


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

import os
import pandas as pd
from thefuzz import fuzz, process

directorio = r"C:\Users\ASUS\Documents\00 Analisis de datos\proyecto"
os.chdir(directorio)

#print("Directorio", os.getcwd())

# print("Directorio de trabajo", os.getcwd())
 
df_ventas = pd.read_csv("Ventas.csv")
 
df_vendedores = pd.read_csv("Vendedores.csv")
 
#print(df_ventas.info())
 
#print(df_vendedores.info())

df_ventas["empresa"] = df_ventas["empresa"].str.lower().str.strip()
df_vendedores["empresa"] = df_vendedores["empresa"].str.lower().str.strip()

def encontrar_mejor_match(nombre, lista_empresas):
    mejor_match, score = process.extractOne(nombre, lista_empresas, scorer=fuzz.token_sort_ratio)
   
    print(score)
    return mejor_match if score > 50 else None
 
df_ventas["empresa_corregida"] = df_ventas["empresa"].apply(lambda x : encontrar_mejor_match(x, df_vendedores["empresa"].tolist()))
 
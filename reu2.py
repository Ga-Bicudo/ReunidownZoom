import requests
import json
import testeapi

res = testeapi.acessarapi().json() #conn.jason()

def calculopag():
    if res['page_count'] > res['page_number']:
       npzoom = res['page_number']
       while npzoom < res['page_count']:
           npzoom = npzoom + 1
           return(npzoom)
           
res2 = testeapi.acessarapi2().json()

lista_contas = res['accounts'] 

  
print(type(lista_contas))

print(len(lista_contas))

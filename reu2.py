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
    def calculapagsize():
        z = res['page_size']
        x = (res['total_records'] - z)
        while x <= 0:
           y = x - z
           x = y 
           print(x)
           return() 
        
           
for paginasjson in [testeapi.acessarapi2().json()]:
    print([paginasjson], "/n")

#print(res)
#lista_contas = res['accounts'] 

  
#print(type(lista_contas))

#print(len(lista_contas))

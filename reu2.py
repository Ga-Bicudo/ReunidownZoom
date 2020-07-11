import requests
import json
import testeapi


res = testeapi.acessarapi().json() #conn.jason()

def calculopag():#verifica se o numero de paginas e maior que o numero da pagina atual, se sim ele da como parametro no acessarapi2 o numero da prox pag para coletar
    if res['page_count'] > res['page_number']:
       npzoom = res['page_number']
       while npzoom < res['page_count']:
           npzoom = npzoom + 1
           return(npzoom)
    def calculapagsize():#calcula o pagsize necessário da ultima pagina
        z = res['page_size'] #300
        x = res['total_records'] #380
        while x > 0:
           y = x - z
           x = y 
           if x > 0 and x < z:
               continue
           return(x) 
        
for paginasjson in [testeapi.acessarapi2().json()]:
    print([paginasjson], "/n")

#print(res)
#lista_contas = res['accounts'] 

  
#print(type(lista_contas))

#print(len(lista_contas))

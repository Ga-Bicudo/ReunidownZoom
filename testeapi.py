import json
import requests

key = "Bearer xxx"
headers = { 'authorization': key}
conn = requests.request("GET", "https://api.zoom.us/v2/accounts", headers=headers, params={'page_number':1}).json()

#print(conn)

n_pag = conn['page_number']

paginas = conn['page_count']

lista_subcontas = []

def acessarapi(n_pag):  #apenas acesa a api e retorna o resultado
    numpag = {'page_number':n_pag}
    conn = requests.request("GET", "https://api.zoom.us/v2/accounts", headers=headers, params=numpag).json()
    contas = conn['accounts']
    
    for i in contas: # i é cada dict que guarda a informação de cada conta.
        lista_subcontas.append(i) #adiciona todas as contas em uma somente lista.
    return

while n_pag <= paginas:
    acessarapi(n_pag)
    ###print("pagina numero:",n_pag)
    n_pag = n_pag + 1

   
   
print(len(lista_subcontas))


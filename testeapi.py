import json
import requests

key = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOm51bGwsImlzcyI6InlDa3J1azhtU0J1OFhVb3JqbWhKemciLCJleHAiOjE1OTk3NjY5MjAsImlhdCI6MTU5OTE2MjEyMH0.P1_J61eyRXv_JQuUx0tl4cNlTZ_iEr-xiijeOgrbRsg"
headers = { 'authorization': key}
conn = requests.request("GET", "https://api.zoom.us/v2/accounts", headers=headers, params={'page_number':1}).json()

#print(conn)

n_pag = conn['page_number']

paginas = conn['page_count']

lista_paginas = []

lista_subcontas = []

def acessarapi(n_pag):  #apenas acesa a api e retorna o resultado
    numpag = {'page_number':n_pag}
    conn = requests.request("GET", "https://api.zoom.us/v2/accounts", headers=headers, params=numpag).json()
    contas = conn['accounts']
    
    for i in contas: # i é cada dict que guarda a informação de cada conta.
        """print("\n")
        print(i)"""
        lista_subcontas.append(i) #adiciona todas as contas em uma somente lista.
        """for j in i:
            print(j,"=",i[j])"""
    return

while n_pag <= paginas:
    acessarapi(n_pag)
    ###print("pagina numero:",n_pag)
    n_pag = n_pag + 1
    
print(lista_subcontas)
print(len(lista_subcontas))

#precisa apenas adicionar todos clientes em uma lista, 
# cada cliente c seu indice e depois fazer um looping inserindo cada um em uma posição do banco
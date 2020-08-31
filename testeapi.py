import json
import requests

key = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOm51bGwsImlzcyI6InlDa3J1azhtU0J1OFhVb3JqbWhKemciLCJleHAiOjE1OTg5MDc1NjAsImlhdCI6MTU5ODkwMjE2MX0.iO0-2LF1_Dle8_sZ-2w4nghfUG_xz9Ky2nNzvYHBpuI"
headers = { 'authorization': key}
conn = requests.request("GET", "https://api.zoom.us/v2/accounts", headers=headers, params={'page_number':1}).json()

n_pag = conn['page_number']

paginas = conn['page_count']

lista_paginas = []

lista_subcontas = []

def acessarapi(n_pag):  #apenas acesa a api e retorna o resultado
    numpag = {'page_number':n_pag}
    conn = requests.request("GET", "https://api.zoom.us/v2/accounts", headers=headers, params=numpag).json()
    contas = conn['accounts']
    
    for i in contas:
        print("\n")
        for j in i:
            print(j,"=",i[j])


    ###testeapi.lista_subcontas.append()
    print(len(contas))  
    return

while n_pag <= paginas:
    acessarapi(n_pag)
    print("pagina numero:",n_pag)
    n_pag = n_pag + 1
    


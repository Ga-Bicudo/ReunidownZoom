import requests
import json
import testeapi


def acessarapi(n_pag):  #apenas acesa a api e retorna o resultado
    numpag = {'page_number':n_pag}
    conn = requests.request("GET", "https://api.zoom.us/v2/accounts", headers=testeapi.headers, params=numpag).json()
    contas = conn['accounts']
    
    for i in contas:
        print[i, '\n']

    ###testeapi.lista_subcontas.append()
    print(len(contas))  
    return(conn)



import json
import requests
import reu2

key = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ5Q2tydWs4bVNCdThYVW9yam1oSnpnIiwiZXhwIjoxNDk2MDkxOTY0MDAwfQ.XhXx65hbXEa8mBPcW7CNxsgxSGTKHhEws8bM3ncxMHo"

def acessarapi():  #apenas acesa a api e retorna o resultado
    headers = { 'authorization': key}
    numpag = {'page_number':1}
    conn = requests.request("GET", "https://api.zoom.us/v2/accounts", headers=headers, params=numpag)  
    return(conn)

def acessarapi2():#apenas acesa a api e retorna o resultado se houver mais de uma pagina para ser guardada
    headers = { 'authorization': key }
    numpag = {'page_size': reu2.calculapagsize() ,'page_number':reu2.calculopag()}
    conn = requests.request("GET", "https://api.zoom.us/v2/accounts", headers=headers, params=numpag)
    print(len(conn.json()['accounts']))
    return(conn)
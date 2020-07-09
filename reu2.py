import requests
import json

def acessarapi():
    headers = { 'authorization': "Bearer " }
    numpag = {'page_size':'300','page_number':npzoom}
    conn = requests.request("GET", "https://api.zoom.us/v2/accounts", headers=headers, params=numpag)
    return(conn)

res = acessarapi().json() #conn.jason()

def acessarapi2():
    if res['page_number'] < res['page_count']:
        

#ordem = json.loads(res)


"""for accounts in [res]:
     print("id:",[id])"""

lista_contas = res['accounts'] 

  
print(type(lista_contas))

print(len(lista_contas))

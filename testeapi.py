import json
import requests
import reu2


def acessarapi():
    headers = { 'authorization': "Bearer xxx" }
    numpag = {'page_size':'300','page_number':1}
    conn = requests.request("GET", "https://api.zoom.us/v2/accounts", headers=headers, params=numpag)
    return(conn)

def acessarapi2():
    headers = { 'authorization': "Bearer xxx" }
    numpag = {'page_size':'300','page_number':reu2.calculopag()}
    conn = requests.request("GET", "https://api.zoom.us/v2/accounts", headers=headers, params=numpag)
    return(conn)
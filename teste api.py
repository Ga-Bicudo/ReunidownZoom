import requests

"""response = requests.get('https://viacep.com.br/ws/01001000/json/')
print(response.status_code)
print(response."""

teste = {
  "alg": "HS256",
  "typ": "JWT"
}

print(type(teste))
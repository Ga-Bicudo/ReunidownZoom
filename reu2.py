import http.client

conn = http.client.HTTPSConnection("api.zoom.us")

headers = { 'authorization': "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ5Q2tydWs4bVNCdThYVW9yam1oSnpnIiwiZXhwIjoxNDk2MDkxOTY0MDAwfQ.XhXx65hbXEa8mBPcW7CNxsgxSGTKHhEws8bM3ncxMHo" }

conn.request("GET", "/v2/accounts?page_number=1&page_size=30", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
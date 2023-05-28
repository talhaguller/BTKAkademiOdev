import http.client

conn = http.client.HTTPSConnection("api.collectapi.com")

headers = {
    'content-type': "application/json",
    'authorization': "api-key"
    }

conn.request("GET", "/economy/liveBorsa", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8")) 
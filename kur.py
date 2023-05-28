import http.client

conn = http.client.HTTPSConnection("api.collectapi.com")

headers = {
    'content-type': "application/json",
    'authorization': "apikey 71QXXfV2zSBV0HV0jAMPtQ:6gTmM6n0NkdZeRA8WvcaTC"
    }

conn.request("GET", "/economy/liveBorsa", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8")) 
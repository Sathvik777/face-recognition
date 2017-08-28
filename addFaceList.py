import http.client, urllib.request, urllib.parse, urllib.error, base64
import json

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '',
}

params = urllib.parse.urlencode({

})



body = {
    'name':'sathvik_face',
    'userData': 'User-provided data attached to the face list',
}

json_data = json.dumps(body)


try:
    print("here TRY")
    conn = http.client.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
    print("here conn")
    conn.request("PUT", "/face/v1.0/facelists/sathvik_face_test1?%s" % params, json_data, headers)
    response = conn.getresponse()
    data = response.read()
    print("printing data")
    print(data)
    conn.close()
except Exception as e:
    print("Errno")

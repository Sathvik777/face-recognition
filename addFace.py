
import http.client, urllib.request, urllib.parse, urllib.error, base64

#{"persistedFaceId":"4fbd5fae-7bfc-48d0-b626-c7906ce7ef69"}'

headers = {
    # Request headers
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': '',
}

params = urllib.parse.urlencode({
    # Request parameters
    'userData': 'testfacedetect'
})
def addImageFile():
    with open("01.png", "rb") as image_file:
        encoded_image = image_file.read()
    try:
        conn = http.client.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
        conn.request("POST", "/face/v1.0/facelists/sathvik_face_test1/persistedFaces?%s" % params, encoded_image, headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        json_obj = json.loads(string)
        print(json_obj['persistedFaceId']) 
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

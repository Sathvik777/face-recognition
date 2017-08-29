import httplib, urllib, base64, json


class detectFace():
    """docstring for ."""
    def __init__(self):
        self.headers = {
            # Request headers
            'Content-Type': 'application/octet-stream',
            'Ocp-Apim-Subscription-Key': '',
        }

        self.params = urllib.urlencode({
            # Request parameters
            'returnFaceId': 'true',
            'returnFaceLandmarks': 'false',
            'returnFaceAttributes': 'age,gender',
        })
        self.faceId = " "




    def generateFaceId(self):
        with open("01.png", "rb") as image_file:
            encoded_image = image_file.read()

        try:
            conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
            conn.request("POST", "/face/v1.0/detect?%s" % self.params, encoded_image, self.headers)
            response = conn.getresponse()

            data = response.read().decode('utf-8')
            print(data)
            json_obj = json.loads(data)
            if(len(json_obj)>0) :

                print(json_obj)
                faceIdArray = json_obj[0]
                faceId = faceIdArray['faceId']
                self.faceId = faceId

                return faceId
            else:
                return " "

            conn.close()

        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))
            return " "

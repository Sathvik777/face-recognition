import httplib, urllib, base64, json
from detectFace import detectFace


class findSimilar():
    """docstring for ."""
    def __init__(self):
        self.headers = {
            # Request headers
            'Content-Type': 'application/json',
            'Ocp-Apim-Subscription-Key': '{}',
        }

        self.params = urllib.urlencode({
        })

        detFac = detectFace()
        faceId = detFac.generateFaceId()
        self.faceId = faceId

        body = {
            "faceId":faceId,
            "faceListId":"sathvik_face_test1",
            "maxNumOfCandidatesReturned":2,
            "mode": "matchPerson"
        }

        self.json_data = json.dumps(body)


    def findName(self):
        try:
            conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
            conn.request("POST", "/face/v1.0/findsimilars?%s" % self.params, self.json_data, self.headers)
            response = conn.getresponse()
            data = response.read().decode('utf-8')
            json_obj = json.loads(data)
            if(len(json_obj)>0) :
                faceIdArray = json_obj[0]

                persistedFaceId = faceIdArray['persistedFaceId']

                confidence = faceIdArray['confidence']
                #get get comapred face ID as attribute
                if persistedFaceId == "0c0d58c5-fbbf-45f5-a6de-62a3a4405b0c" and confidence > 0.7:
                    print("SATHVIK")

                elif persistedFaceId == " ":
                    print("SEARCHING FOR FACE")
                else :
                    print("NOT SATHVIK")

                return 1

            else :
                print("LAUNCHING....")

                return 0



            conn.close()
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))

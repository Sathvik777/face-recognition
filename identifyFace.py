import httplib, urllib, base64,json


class identifyFace():
  def __init__(self):
    self.headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': 'cabe9cc156a444719988547fc783285d',
    }

    self.params = urllib.urlencode({
    })



  def identifyFaceIds(self, faceIds):
    body = {
      "personGroupId":"mobileinteraction",
      "faceIds":faceIds,
      "maxNumOfCandidatesReturned":2,
      "confidenceThreshold": 0.5
    }
    json_data = json.dumps(body)

    try:
      conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
      conn.request("POST", "/face/v1.0/identify?%s" % self.params, json_data, self.headers)
      response = conn.getresponse()
      data = response.read()
      print(data)
      conn.close()
    except Exception as e:
      print("[Errno {0}] {1}".format(e.errno, e.strerror))
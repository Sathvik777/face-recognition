import httplib, urllib, base64, json
from detectFace import detectFace
import datetime,time

class verifyFace():
  def __init__(self):
    self.headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': 'cabe9cc156a444719988547fc783285d',
    }


    self.params = urllib.urlencode({
      })



  def verifyFaceId(self):
    detFac = detectFace()
    faceId = detFac.generateFaceId()

    if(faceId == " "):
      print("SEARCHING FOR FACE")
      return 0


    body = {
            "faceId":faceId,
            "personId":"87b23e0c-41fe-4012-8e18-a5c9d649d8f2",
            "personGroupId":"mobileinteraction"
            }
    json_data = json.dumps(body)

    try:
      conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
      conn.request("POST", "/face/v1.0/verify?%s" % self.params, json_data, self.headers)
      response = conn.getresponse()
      data = response.read()
      json_obj = json.loads(data)
      if(json_obj is not None) :
        isIdentical = json_obj['isIdentical']
        confidence = json_obj['confidence']
        #get get comapred face ID as attribute
        if isIdentical and confidence > 0.7:
            print("SATHVIK")

        else :
          print("NOT SATHVIK")

        ts = time.time()
        print(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
        return 1

      else :
        print("SEARCHING FOR FACE")
        ts = time.time()
        print(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
        return 0

      conn.close()

    except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))

import httplib, urllib, base64,json
import os, errno


class identifyFace():
  def __init__(self):
    self.headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': 'cabe9cc156a444719988547fc783285d',
    }

    self.params = urllib.urlencode({
    })

    self.personsList = {
      '87b23e0c-41fe-4012-8e18-a5c9d649d8f2': 'Sathvik',
      'a07f183e-d2d8-4782-9c09-d847122e81d3': 'Zintis',
      'fac39ace-374d-4b89-9ba9-190d3ff994ec' : 'Victor'
     }



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

      response_body_array = json.loads(data)

      try :
        response_body = response_body_array[0]
      except Exception:
        print("let me try again ")
        return 0

      try :
        faces_in_response = response_body['candidates']
      except Exception:
        print("let me try again ")
        return 0


      print(faces_in_response)
      if(len(faces_in_response)>0) :
        face_found = faces_in_response[0]
        personId = face_found['personId']
        confidence = face_found['confidence']
        if personId in self.personsList  and confidence > 0.7:

          print("{1} {0}".format(confidence, self.personsList[personId]))

        else :
          print("NOT found {0} but could be {1}".format(confidence, personId))

        os.remove("01.png")

        return 1

      else:
        print("searching for face again....")

        return 0

      conn.close()
    except Exception as e:
      print("[Errno {0}] {1}".format(e.errno, e.strerror))
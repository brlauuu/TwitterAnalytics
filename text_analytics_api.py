import httplib, urllib, base64, json

class TextAnalyticsApi:
    def __init__(self):
        self.ta_key = ""
        self.LoadCredentials()

    def LoadCredentials(self):
        # Read Text Analytics API
        with open('.credentials/text-analytics-api-credentials') as ta_api_credentials:
            self.ta_key = ta_api_credentials.readline()

    def GetSentiment(self, tweets, language):
        # Write data to json file
        inputData = {}
        inputData["documents"] = []
        id = 0
        for twt in tweets:
            tmp = {}
            tmp["id"] = id
            tmp["text"] = twt.text.encode('utf8')
            tmp["language"] = language
            id += 1
            inputData["documents"].append(tmp)

        inputJson = json.dumps(inputData)
        inputJson = str(inputJson.encode('utf8'))

        headers = {
            # Request headers
            'Content-Type': 'application/json',
            'Ocp-Apim-Subscription-Key': self.ta_key,
        }

        params = urllib.urlencode({
        })

        try:
            # Make a request
            conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
            conn.request("POST", "/text/analytics/v2.0/sentiment?%s" % params, inputJson, headers)
            response = conn.getresponse()
            data = response.read()
            data = json.loads(data)
            
            if ('documents' not in data):
                raise Exception(data["code"] + " : " + data["message"])
            conn.close()

        except Exception as e:
            data = None
            print 'Please verify your Microsoft Cognitive Services API key, this one doesn\'t work.'

        return data

        






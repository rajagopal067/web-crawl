import urllib2
import json
import codecs

def queryAPI(url,payload,reviewDesc,count,responseFile):
    req=urllib2.Request(url,payload)
    response=urllib2.urlopen(req)
    jsonOutput=json.loads(response.read())
    jsonOutput["reviewDesc"]=reviewDesc
    jsonOutput["count"]=count
    responseFile.write(json.dumps(jsonOutput,indent=4)+"\n")
    print(jsonOutput)


url="http://text-processing.com/api/sentiment/"
reviewsFile = codecs.open("reviewsFile.txt",'r')
responseFile =codecs.open("response.txt",'w')
data = json.load(reviewsFile)

reviews = data["reviews"]

for review in reviews:
    desc = review["desc"].encode('ascii','ignore')
    queryAPI(url,"text="+desc,desc,review["count"],responseFile)
responseFile.close()
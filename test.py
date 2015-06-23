import json

'''
data={}
data["reviews"]=[]
review1={}
review1["count"]=1
review1["desc"]="This is good"
review2={}
review2["count"]=2
review2["desc"]="This is bad"

data["reviews"].append(review1)
data["reviews"].append(review2)
print data
file = open("r.txt","w")
file.write(json.dumps(data,indent=4))
'''

#!/usr/bin/python
# -*- coding: utf-8 -*-


def kml2latlong(kml):
    kmlList = kml[25:-27].split(',')

    jsonArray = []
    lat_list = []
    long_list = []
    for (index, value) in enumerate(kmlList):
        if index % 2 == 0 and value != '0':
            valueList = value.split(' ')
            if len(valueList) > 1:
                lat = valueList[1]
            else:
                lat = valueList[0]
            lat_list.append(lat)
        elif value != '0':
            long_list.append(value)

    for (lat, long) in zip(lat_list, long_list):
        jsonArray.append({'lat': str(lat), 'long': str(long)})


    return jsonArray





kml="<LineString><coordinates>41.7627045,-72.6818108,0 41.7625855,-72.6818751,0 41.7625013,-72.681905,0 41.7624128,-72.6819259,0 41.7623272,-72.6819424,0 41.7622391,-72.6819499,0 41.7621431,-72.6819392,0 41.7619903,-72.6819023,0</coordinates></LineString>"

kmlList = kml[25:-27].split(',')

jsonArray = []

lat_list = []
long_list = []
for index,value in enumerate(kmlList):
    if index % 2 == 0 and value != '0':
        valueList = value.split(' ')
        if len(valueList) > 1:
            lat = valueList[1]
        else:
            lat = valueList[0]
        lat_list.append(lat)
    elif value != '0':
        long_list.append(value)


for lat,long in zip(lat_list,long_list):
    jsonArray.append({"lat":lat,"long":long})

print jsonArray
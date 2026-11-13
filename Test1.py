import requests
import random
import os
from datetime import date
from datetime import time
import calendar

APIfile=open("./.venv/APIkeyDoc","r")
APIkey=APIfile.readline()
response=requests.get("https://data.hub.api.metoffice.gov.uk/sitespecific/v0/point/hourly?excludeParamterMetadata=true&includeLocationName=true&latitude=53.788123&longitude=-1.528409",headers = {
    "ApiKey": APIkey})
print(response.status_code)
#print(response.text)
#fullResponse = response.text

responseAsJSON=response.json()
print(responseAsJSON['features'][0]['properties']['modelRunDate'])
print(responseAsJSON['features'][0]['properties']['timeSeries'][0])
print(responseAsJSON['features'][0]['properties']['timeSeries'][0]['screenTemperature'])

def RandomMessage(messageType):
    messageDict={"BasicGreetings":0,"windMSGnot":10,"windMSGslight":20,"wingMSGwindy":30,"windMSGvery":40,"windMSGBad":50,
                 "tempMSGfreezing":60,"tempMSGunder5":70,"tempMSGunder10":80,"tempMSGunder15":90,"tempMSGunder20":100,"tempMSGunder25":110,
                 "rainMSGdry":120,"rainMSGunder20":120,"rainMSGunder40":130,"rainMSGunder50":140,"rainMSGunder75":150,"rainMSGunder100":160,
                 }
    lowerbound=messageDict[messageType]+1
    upperbound=messageDict[messageType]+9
    SelectedMessage=random.randint(lowerbound,upperbound)
    FileMethod=open("C:/Users/peter/PycharmProjects/MetOfficeAPIstuff/Messages",'r')
    lineCounter=0
    while lineCounter<SelectedMessage:
        text=FileMethod.readline()
        lineCounter+=1
    print(text)


if float(responseAsJSON['features'][0]['properties']['timeSeries'][0]['windGustSpeed10m']) < 0.00:
    RandomMessage("windMSGnot")
elif float(responseAsJSON['features'][0]['properties']['timeSeries'][0]['windGustSpeed10m']) < 5.00:
    print("slight breeze")
elif float(responseAsJSON['features'][0]['properties']['timeSeries'][0]['windGustSpeed10m']) < 10.00:
    print("windy")
elif float(responseAsJSON['features'][0]['properties']['timeSeries'][0]['windGustSpeed10m']) < 20.00:
    print("quite windy")
else:
    print("I wouldn't")


if float(responseAsJSON['features'][0]['properties']['timeSeries'][0]['screenTemperature']) < 0.00:
    print("it is literally freezing")
elif float(responseAsJSON['features'][0]['properties']['timeSeries'][0]['screenTemperature']) < 5.00:
    print("very cold right now")
elif float(responseAsJSON['features'][0]['properties']['timeSeries'][0]['screenTemperature']) < 10.00:
    print("rather chilly")
elif float(responseAsJSON['features'][0]['properties']['timeSeries'][0]['screenTemperature']) < 15.00:
    print("alright")
elif float(responseAsJSON['features'][0]['properties']['timeSeries'][0]['screenTemperature']) < 20.00:
    print("warm")
else:
    print("hot")


if float(responseAsJSON['features'][0]['properties']['timeSeries'][0]['probOfPrecipitation']) < 0.00:
    print("dry right now")
elif float(responseAsJSON['features'][0]['properties']['timeSeries'][0]['probOfPrecipitation']) < 20.00:
    print("probably won't rain")
elif float(responseAsJSON['features'][0]['properties']['timeSeries'][0]['probOfPrecipitation']) < 40.00:
    print("might rain")
elif float(responseAsJSON['features'][0]['properties']['timeSeries'][0]['probOfPrecipitation']) < 50.00:
    print("could rain")
elif float(responseAsJSON['features'][0]['properties']['timeSeries'][0]['probOfPrecipitation']) < 75.00:
    print("likely will rain")
elif float(responseAsJSON['features'][0]['properties']['timeSeries'][0]['probOfPrecipitation']) < 100.00:
    print("probably will rain")
else:
    print("hmmm")

print("welcome to handles")
print("another test")
#print(date.today())
todaysdate=date.today()
dateAsList=todaysdate.strftime("%Y.%m.%d")
dateAsList=dateAsList.split(".")
#print(dateAsList)
today=calendar.weekday(int(dateAsList[0]),int(dateAsList[1]),int(dateAsList[2]))
daysOFweek={0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}
months={1:"January",2:"Febuary",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
print("Today is",daysOFweek[today], "the", int(dateAsList[2]))
print(str(daysOFweek[today])+", "+str(int(dateAsList[2]))+", "+str(months[int(dateAsList[1])]))

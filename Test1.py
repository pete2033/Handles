import requests
import random
import os

response=requests.get("https://data.hub.api.metoffice.gov.uk/sitespecific/v0/point/hourly?excludeParamterMetadata=true&includeLocationName=true&latitude=53.788123&longitude=-1.528409",headers = {
    "ApiKey": "eyJ4NXQjUzI1NiI6Ik5XVTVZakUxTkRjeVl6a3hZbUl4TkdSaFpqSmpOV1l6T1dGaE9XWXpNMk0yTWpRek5USm1OVEE0TXpOaU9EaG1NVFJqWVdNellXUm1ZalUyTTJJeVpBPT0iLCJraWQiOiJnYXRld2F5X2NlcnRpZmljYXRlX2FsaWFzIiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYifQ==.eyJzdWIiOiJwZXRlckBoYXJyaXNlbWFpbC51a0BjYXJib24uc3VwZXIiLCJhcHBsaWNhdGlvbiI6eyJvd25lciI6InBldGVyQGhhcnJpc2VtYWlsLnVrIiwidGllclF1b3RhVHlwZSI6bnVsbCwidGllciI6IlVubGltaXRlZCIsIm5hbWUiOiJzaXRlX3NwZWNpZmljLWYyNjZkNzFmLTNhMWUtNGM2Zi1iZTVlLWJiNGNmNzZkYjc0OCIsImlkIjo2ODE0OCwidXVpZCI6IjAzMmMwMTM2LTkzNTMtNDBkYi1hNzQ1LTRhYzczZjExNDE3NyJ9LCJpc3MiOiJodHRwczpcL1wvYXBpLW1hbmFnZXIuYXBpLW1hbmFnZW1lbnQubWV0b2ZmaWNlLmNsb3VkOjQ0M1wvb2F1dGgyXC90b2tlbiIsInRpZXJJbmZvIjp7IndkaF9zaXRlX3NwZWNpZmljX2ZyZWUiOnsidGllclF1b3RhVHlwZSI6InJlcXVlc3RDb3VudCIsImdyYXBoUUxNYXhDb21wbGV4aXR5IjowLCJncmFwaFFMTWF4RGVwdGgiOjAsInN0b3BPblF1b3RhUmVhY2giOnRydWUsInNwaWtlQXJyZXN0TGltaXQiOjAsInNwaWtlQXJyZXN0VW5pdCI6InNlYyJ9fSwia2V5dHlwZSI6IlBST0RVQ1RJT04iLCJzdWJzY3JpYmVkQVBJcyI6W3sic3Vic2NyaWJlclRlbmFudERvbWFpbiI6ImNhcmJvbi5zdXBlciIsIm5hbWUiOiJTaXRlU3BlY2lmaWNGb3JlY2FzdCIsImNvbnRleHQiOiJcL3NpdGVzcGVjaWZpY1wvdjAiLCJwdWJsaXNoZXIiOiJKYWd1YXJfQ0kiLCJ2ZXJzaW9uIjoidjAiLCJzdWJzY3JpcHRpb25UaWVyIjoid2RoX3NpdGVfc3BlY2lmaWNfZnJlZSJ9XSwidG9rZW5fdHlwZSI6ImFwaUtleSIsImlhdCI6MTc5MjI3OTg0OCwianRpIjoiN2M5ZDRjZjQtNTIxZi00YjdmLWFmYzUtY2RmZDMwM2NlYWQwIn0=.ERfwf0jr-T2-ohl1qYoKBYiVtKDOetDGJcbF10meKrmv-KNRGGM42_XW46i56ybHJOmd1H3zHtPq6p1HxgW1HK0GuMUThJt4Lba5PJZlHAPnI1obN8vK9TnHCzZckkyW03KSW9FvU0Gx8od-eq3R9jynESzbodIBeN6rs5dhqhdhzRtkRNDEun6GBQG1aPRLXg7Eu5y18a0BwuwkakJeiPs5wzziXNbKDguodQfnK8VQFGGVS8oLtE8PfSrsAkYZ7TX7_tUmdMRw_RZ-BiWbZME6Odi4LK_sVYgjr6DBYmTbbz9ppwgNeM6DuQvVvuFa2HM0odtrCfOgwnyc_ovBvg==",
"datetime":"2026-10-23T11:00Z"})
print(response.status_code)
#print(response.text)
#fullResponse = response.text

responseAsJSON=response.json()
print(responseAsJSON['features'][0]['properties']['modelRunDate'])
print(responseAsJSON['features'][0]['properties']['timeSeries'][0])
print(responseAsJSON['features'][0]['properties']['timeSeries'][0]['screenTemperature'])

def RandomMessage(messageType):
    messageDict={"greetings":0,"windMSG":10,"tempMSG":20,"rainMSG":30}
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
    print("it is not windy")
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
    print("could be worse")
elif float(responseAsJSON['features'][0]['properties']['timeSeries'][0]['screenTemperature']) < 20.00:
    print("not bad")
else:
    print("warm")


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
RandomMessage("greetings")
RandomMessage("windMSG")
RandomMessage("rainMSG")
RandomMessage("tempMSG")

#if float(responseAsJSON['features'][0]['properties']['timeSeries'][0]['totalPrecipAmount']):
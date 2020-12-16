import requests
import json


def linkInput():
    """ Use for user input link to short """
    startLink = str(input("Enter your link for short: "))
    
    return startLink


def checkInput(startLink):
    """ Use for check user input and correct if need """
    if "bitly.com" in startLink:
        print("Service can't short link cantained 'bitly.com' in any condition.")
        startLink = str(input("Enter your link for short: "))

    if startLink[:5] not in ["https", "http:"]:
        startLink = f"http://{startLink}"
    
    return startLink


def short(startLink):
    """ TOKEN and group_guid you can get after register on bitly.com """
    headers = {
        'Authorization': 'Bearer {TOKEN}',
        'Content-Type': 'application/json',
    }

    data = '{"long_url": "xxx", "domain":"bit.ly", "group_guid": "{group_guid}"}'
    data = data.replace("xxx", startLink) #replaing xxx in previous string on user input data  
    
    try:
        response = requests.post("https://api-ssl.bitly.com/v4/shorten", headers=headers, data=data)
        res = json.loads(response.text)
        return res["link"]
    except KeyError as ke:
        print(ke)
    except UnicodeEncodeError as ue:
        print(ue)
    
startLink = checkInput(linkInput())

print(f"Your shorten link is - {short(startLink)}")

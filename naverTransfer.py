import urllib.request
import requests

def useTransferRequest(myText):
    client_id = "EaBL8hrr09nHEHiI3JGt"
    client_secret = "8SpAPuQEXb"
    encText = urllib.parse.quote(myText)
    data = "source=en&target=ko&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"

    headers = {
        'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Naver-Client-Id': client_id,
        'X-Naver-Client-Secret':client_secret
    }
    res = requests.post(url=url, headers=headers, data=data.encode("utf-8"))
    return res.status_code, res.json()




def useTransfer(myText):
    client_id = "vwgan_9XCoB3MeK4wqEZ"
    client_secret = "Fa8lOIxI0W"
    encText = urllib.parse.quote(myText)
    data = "source=en&target=ko&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        return response_body.decode('utf-8')
    else:
        return ("Error Code:" + rescode)
import sys
import requests
client_id = "n7zz4t1epm"
client_secret = "gmtPHxEKgVOJS8U7SI3yfq6fcFkqfoLxuZmNf8rb"
lang = "Kor" # 언어 코드 ( Kor )
url = "https://naveropenapi.apigw.ntruss.com/recog/v1/stt?lang=" + lang
data = open('recorded_audio.wav', 'rb')
headers = {
    "X-NCP-APIGW-API-KEY-ID": client_id,
    "X-NCP-APIGW-API-KEY": client_secret,
    "Content-Type": "application/octet-stream"
}
response = requests.post(url,  data=data, headers=headers)
rescode = response.status_code
if(rescode == 200):
    print (response.text)
else:
    print("Error : " + response.text)
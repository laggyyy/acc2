import amino
import os
import json
import threading
import requests
import wget
import heroku3
key="7ad5b9cf-7c8c-4ff5-a016-6186e636d3b7"
nickname="Charlie"
app_name="acc1222"
url="https://samar.thehybridklaus.repl.co"
password="samar123"
def restart():
    heroku_conn = heroku3.from_key(key)
    botapp= heroku_conn.apps()[app_name]
    botapp.restart()
def send(data):
    requests.post(f"{url}/save",data=data)
client=amino.Client("32FEAC855F12401A9D469D1607748BA32A63B83187663F8B3CCB1223D68067E7B2829497E2645B6741")

def codee(link):
	d={"data":link}
	p=requests.post("http://192.46.210.24:5000/captcha",data=d)
	return p.json()["dick"]

#password=custompwd

for i in range(3):
  dev=client.devicee()
  #dev=client.device_id
  email=client.gen_email()
  print(email)
  client.request_verify_code(email = email,dev=dev)
  link=client.get_message(email)
  try: code=codee(link)
  except: pass
  
  
  try:
    client.register(email = email,password = password,nickname =nickname, verificationCode = code,deviceId=dev)
    #sub.send_message(chatId=chatId,message="Criada")
    d={}
    d["email"]=str(email)
    d["password"]=str(password)
    d["device"]=str(dev)
    t=json.dumps(d)
    data={"data":t}
    send(data)
  except Exception as l:
    print(l)
    pass


restart()

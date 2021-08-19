import requests as req
import json
import re as Regex

regex = r"/watch\?v=[\w\d_-]+"
Headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
    "accept": "text/html,application/json",
    "Cookie": "CONSENT=YES+cb.20210813-05-p0.en+FX+867"
}
print("+loading config ...")
with open('players.json', encoding="utf8") as json_data:
    players = json.load(json_data)
print("+Clearing output ...")
with open('output.bat', mode="w", encoding="utf8") as file:
    file.write("")

baseURL = "https://www.youtube.com"

print("+loading history ...")
with open('history.txt', mode="r", encoding="utf8") as file:
    history = file.readlines()

print("+opening a session...")
session = req.session()
session.headers = Headers

for i in players:
    datalink = str(players[i]).split(",")
    count = int(datalink[0])
    data = session.get(datalink[1])
    print("getting links :"+str(data.status_code))
    links = Regex.findall(regex, data.text)
    for i in range(0, count):
        link = baseURL + links[i]
        enable = True
        for L in history:
            M = L.replace("\n", "")
            if link == M:
                enable = False
                break
        if enable:
            print("hit a video")
            with open('output.bat', mode="a", encoding="utf8") as file:
                file.write("pytube "+link+"\n")
            with open('history.txt', mode="a", encoding="utf8") as file:
                file.write(link+"\n")
session.close()

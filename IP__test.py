import requests
import time
# url = "http://icanhazip.com/"
url = "http://pv.sohu.com/cityjson?ie=utf-8"
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
f = open("ip_list.txt",'r')
g = open("ip_OK.txt",'w')
for i in f.readlines()[:30]:
    proxy = i.rstrip()
    print(proxy)
    proxies = {'http': proxy}
    try:
        time.sleep(3)
        r = requests.get(url=url, proxies=proxies, headers=headers, timeout=5)
        time.sleep(3)
        print(r.status_code)
        print(r.text)
        g .write(proxy+'\n')
    except Exception:
        print("-------------FCUK!!!!!!______________")
f.close()
g.close()





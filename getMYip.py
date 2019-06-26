import requests,json
url = "http://ip.taobao.com/service/getIpInfo.php"
data = {"ip":"myip"}
r = requests.post(url,data=data)
ipinfo = json.loads(r.text)['data']['ip']
print(ipinfo)

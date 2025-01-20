import requests 

url_params = {'name': 'JUstiN', 'score': 95}
r = requests.get("http://httpbin.org/get", params=url_params)
print(r.url)
param1='name'
value1='JUstin'
param2='score'
value2='98'
url_params_str=f"http://httpbin.org/get?{param1}={value1}&{param2}={value2}"
rr=requests.get(url_params_str)
print(rr.text)
import pandas as pd
import requests, json, xmltodict

service_key="use your keys(go to data.go.kr)"
base_url='http://newsky2.kma.go.kr/service/VilageFrcstDspthDocInfoService/WidOverlandForecast?regId=11A00101&ServiceKey={0}'.format(service_key)
js = requests.get(base_url)

dc = xmltodict.parse(js.text)
df = pd.read_json(json.dumps(dc))

rain = list()
temp = list()
for json_data in df["response"]["body"]["items"]["item"]:
    if json_data["rnSt"]:
        print('rain', json_data["rnSt"])
        rain.append(float(json_data["rnSt"]))
    if json_data.__contains__('ta'):
        print('temp', json_data["ta"])
        temp.append(float(json_data["ta"]))
    else:
        print('temp', None)
        temp.append(None)


ans = pd.DataFrame()
ans["rain"] = rain
ans["temp"] = temp

ans.to_csv("ans.csv")
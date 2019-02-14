import pandas as pd
import requests, json, xmltodict
from datetime import datetime

service_key="(use your key)"
base_url='http://newsky2.kma.go.kr/service/VilageFrcstDspthDocInfoService/WidOverlandForecast?regId=11A00101&ServiceKey={0}'.format(service_key)
js = requests.get(base_url)

dc = xmltodict.parse(js.text)
df = pd.read_json(json.dumps(dc))

print(df["response"]["body"]["items"]["item"])

rain = list()
temp = list()
wsIt = list()
wfCd = list()
for json_data in df["response"]["body"]["items"]["item"]:
    if json_data.__contains__('rnSt'):
        rain.append(float(json_data["rnSt"]))
    else:
        rain.append(None)

    if json_data.__contains__('ta'):
        temp.append(float(json_data["ta"]))
    else:
        temp.append(None)

    if json_data.__contains__('wsIt'):
        wsIt.append(float(json_data["wsIt"]))
    else:
        wsIt.append(None)

    if json_data.__contains__('wfCd'):
        wfCd.append(float(json_data["wfCd"][-1]))
    else:
        wfCd.append(None)

ans = pd.DataFrame()
ans["rain"] = rain
ans["temp"] = temp
ans["wsIt"] = wsIt
ans["wfCd"] = wfCd

ans.to_csv("{}.csv".format(datetime.now().strftime("%Y%m%d%HH%MM")))
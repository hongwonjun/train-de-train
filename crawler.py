import requests, json, configparser, sys
from datetime import datetime, timedelta

config = configparser.ConfigParser()
config.read('config.cfg')

keyname = sys.argv[1]
authkey = config['authkey'][keyname]

URL = f'http://swopenAPI.seoul.go.kr/api/subway/{authkey}/json/realtimePosition/0/100/경의중앙선'
response = requests.get(URL)

if response.status_code == 200:
  thistime = datetime.today()
  delta = timedelta(hours=9)
  
  filename = (thistime + delta).strftime("%Y-%m-%d-%H-%M-%S")
  json_data = response.json()
  with open(f'./data/{filename}.json', 'w') as outfile:
    json.dump(json_data['realtimePositionList'], outfile, indent=2)

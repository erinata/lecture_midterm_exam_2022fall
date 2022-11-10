import pandas
import os
import math
import requests
import json
import time


if not os.path.exists('data_output'):
  os.mkdir('data_output')
  
f = open("token", "r")
token = f.read()
f.close()
  
  
github_session = requests.Session()
github_session.auth = ( "erinata", token)
  
  
github_data = pandas.read_csv("data_input/github_data.csv")

starred_url_list = github_data['starred_url']


# print(starred_url_list)
df = pandas.DataFrame()

for starred_url in starred_url_list:
  print(starred_url)
  if (starred_url=="missing"):
    starred_count = "missing"
  else:
    starred_url = starred_url.replace("{/owner}", "").replace("{/repo}", "")
    response_text = github_session.get(starred_url).text
    json_text = json.loads(response_text)
    starred_count = str(len(json_text))
  df = pandas.concat([df,
  pandas.DataFrame.from_records([{
    'starred_count': str(starred_count)
    }])
  ])
  time.sleep(0.1)
  
df.to_csv("data_output/github_data_starred.csv", index =False)

  
  
import pandas
import os

if not os.path.exists('data_output'):
  os.mkdir('data_output')
  
charcoalpaper_data = pandas.read_csv("data_input/charcoalpaper.csv")
github_data = pandas.read_csv("data_input/github_data.csv")
github_data_starred = pandas.read_csv("data_input/github_data_starred.csv")

charcoalpaper_data = charcoalpaper_data.rename(
  columns={'ghid': 'ghid_charcoalpaper', 
            'repocount': 'repocount_charcoalpaper', 
            'followercount': 'followercount_charcoalpaper', 
            'membersince': 'membersince_charcoalpaper' })

dataset = pandas.concat([github_data, charcoalpaper_data, github_data_starred], axis = 1)


dataset=dataset[dataset['number_id']!="missing"]
print(dataset)
dataset.to_csv("data_output/dataset.csv", index =False)

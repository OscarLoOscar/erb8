# district_choices = {
#   "Islands":"Islands",
#   "Kwai Tsing":"Kwai Tsing",
#   "North":"North",
#   "Sai Kung":'Sai Kung',
#   "Sha Tin":"Sha Tin",
#   "Tai Po":"Tai Po",
#   "Tsuen Wan":"Tsuen Wan",
#   "Tuen Mun":"Tuen Mun",
#   "Yuen Long":"Yuen Long",
#   "Kowloon City":"Kowloon City",
#   "Kwun Tong":"Kwun Tong",
#   "Sham Shui Po":"Sham Shui Po",
#   "Wong Tai Sin":"Wong Tai Sin",
#   "Yau Tsim Mong":"Yau Tsim Mong",
#   "Central & Western":"Central & Western",
#   "Eastern":"Eastern",
#   "Southern":"Southern",
#   "Wan Chai":"Wan Chai",
# }

# sorted_districts = sorted(district_choices.items(),key= lambda x:x[1])

district_groups = {
    "Hong Kong Island": {
        "CW": "Central & Western",
        "ER": "Eastern",
        "SR": "Southern",
        "WC": "Wan Chai",
    },
    "Kowloon": {
        "KC": "Kowloon City",
        "KW": "Kwun Tong",
        "SS": "Sham Shui Po",
        "WT": "Wong Tai Sin",
        "YM": "Yau Tsim Mong",
    },
    "New Territories": {
        "IL": "Islands",
        "KT": "Kwai Tsing",
        "NR": "North",
        "SK": "Sai Kung",
        "ST": "Sha Tin",
        "TP": "Tai Po",
        "TW": "Tsuen Wan",
        "TM": "Tuen Mun",
        "YL": "Yuen Long",
    }
}

district_groups_choices = []
for region , districts in district_groups.items():
  group_list=[]
  for code,name in districts.items():
    group_list.append((code,name))
  district_groups_choices.append((region,tuple(group_list)))
  
bedroom_choices = {
  '1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10
}

room_type_choices = {
  'Private Rooms':'Private Rooms',
  'Semi-Private Rooms':'Semi-Private Rooms',
  'Standard (Multi-bed) Rooms':'Standard (Multi-bed) Rooms'
}
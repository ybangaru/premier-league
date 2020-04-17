import pandas as pd
import csv
import time
import json
import requests
import datetime as dt

subcount = 0
sub_reddit = 'PremierLeague'
beginning = int(dt.datetime(2019, 8, 2, 0,0,0).timestamp())   #13th Aug 2016 beginning of PL
ending = int(dt.datetime(2020, 3, 8, 0, 0, 0).timestamp())   #21st May 2017 last match ofPL
max_num = 1000                                              #Pushshift's allowed limit 
data_dict = {}
            
def getSubData(sub):
    sub_data = list()
    title = sub['title']
    address = sub['url']
    try:
        flair = sub['link_flair_text']
    except KeyError:
        flair = "NaN"
    author = sub['author']
    sub_id = sub['id']
    score = sub['score']
    created = dt.datetime.fromtimestamp(sub['created_utc'])
    num_comments = sub['num_comments']
    permalink = sub['permalink']

    sub_data.append((sub_id,title,address,author,score,created,num_comments,permalink,flair))
    data_dict[sub_id] = sub_data
        
def getPushShiftData(subreddit, beginning, ending, max_num):
    url = 'https://api.pushshift.io/reddit/search/submission/?subreddit='+str(subreddit)+'&size='+str(max_num)+'&after='+str(beginning)+'&before='+str(ending)+'&sort=asc'
    #print(url)
    r = requests.get(url)
    data = json.loads(r.text)
    #while len(data)>0:
    return data['data']

def updateSubs_file(result):
    upload_count = 0
    location = "/home/kaalachasma/Yaswanth/FE/Premier League/data/reddit"
    print("input filename of submission file, please add .csv")
    filename = input()
    file = location + filename
    with open(file, 'w', newline='', encoding='utf-8') as file: 
        a = csv.writer(file, delimiter=',')
        headers = ['sub_id','title','address','author','score','created','num_comments','permalink','flair']
        a.writerow(headers)
        for sub in result:
            a.writerow(result[sub][0])
            upload_count+=1
            
        print(str(upload_count) + " submissions have been uploaded")

result = getPushShiftData(sub_reddit,beginning,ending,max_num)

while len(result)!=0:
    for submission in result:
        #print(submission)
        getSubData(submission)
        subcount = subcount+1
    
    print(len(result))
    print(result[-1]['created_utc'])
    
    beginning = result[-1]['created_utc']
    result = getPushShiftData(sub_reddit,beginning,ending,max_num)


updateSubs_file(data_dict)

#result = getPushShiftData(sub_reddit,beginning,ending,max_num)
#season1 = pl.request_reddit(sub_reddit, beginning, ending, max_num)
#result = season1.getPushShiftData()
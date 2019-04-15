import os
import re
import googleapiclient.discovery
import json
import pandas as pd
import csv
import datetime
import time
import requests
from config import gkey

def get_user_channel(video_id):
    url = 'https://www.youtube.com/oembed'
    
    params = {
        'url' : f'http://www.youtube.com/watch?v={video_id}',
        'format': 'json'
    }
    
    response = requests.get(url=url, params=params)
    
    if response.status_code == 200:
        try:
            result = response.json()

            return result['author_url'].split('/')[-1]
        except:
            return None
    else:
        return None    


def get_api_key(key, response):
    try:
        if key == 'channel_id':
            return response['items'][0]['id']

        elif key == 'publishedAt':
            return response['items'][0]['snippet']['publishedAt']

        elif key == 'subscriberCount':
            return response['items'][0]['statistics']['subscriberCount']

        elif key == 'videoCount':
            return response['items'][0]['statistics']['videoCount']

        elif key == 'viewCount':
            return response['items'][0]['statistics']['viewCount']
        else:
            return 0
    except:
        return 0

def main(debug, partial):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    sleep = 1
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = gkey
    parts = "snippet,contentDetails,statistics"

    source_csv = '../../../resources/datasets/USvideos.csv'
    output_csv = '../../../resources/datasets/USchannels.csv'
    partial_csv = '../../../resources/datasets/partial/partial_channels.csv'

    restart_list = []

    if partial == True:
        reader = csv.DictReader(open(partial_csv, encoding='utf-8'))
        restart_list = [row['video_id'] for row in reader]


    youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey = DEVELOPER_KEY)

    df = pd.read_csv(source_csv)
    record = {}

    with open(file=output_csv, mode='w', newline='', encoding='utf-8') as output_df:
        field_names = ["video_id", "channel_id", "publishedAt", "subscriberCount", "videoCount", "viewCount", "timestamp"]
        
        csv_writer = csv.DictWriter(output_df, fieldnames=field_names, delimiter=',')
        csv_writer.writeheader()

        for video in df['video_id'].unique():
            if video not in restart_list:                
                channel = get_user_channel(video) 
                 
                if channel != None:
                    record['video_id'] = video

                    request = youtube.channels().list(part=parts, forUsername=channel)
                    response = request.execute()

                    if debug == True:
                        print(json.dumps(response, indent=4, sort_keys=True)) 

                    if (response['pageInfo']['totalResults']) > 0:
                        record['channel_id'] = get_api_key('channel_id', response)
                        record['publishedAt'] = get_api_key('publishedAt', response)
                        record['subscriberCount'] = get_api_key('subscriberCount', response)
                        record['videoCount'] = get_api_key('videoCount', response)
                        record['viewCount'] = get_api_key('viewCount', response)
                    else:
                        record['channel_id'] = None
                        record['publishedAt'] = None
                        record['subscriberCount'] = 0
                        record['videoCount'] = 0
                        record['viewCount'] = 0
                    
                    record['timestamp'] = str(datetime.datetime.now())

                    csv_writer.writerow(record)
                    time.sleep(sleep)
                else:
                    print (f'Information not available for video id : {video}')

            else:
                print (f"Video {video} already in dataset. Skipping..")

    print ("Process completed without errors")

if __name__ == "__main__":
    main(debug=False, partial=True) 
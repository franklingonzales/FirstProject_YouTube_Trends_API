import os
import re
import googleapiclient.discovery
import json
import pandas as pd
import csv
import datetime
import time
from config import gkey

# check video
#   https://www.youtube.com/watch?v=<video_id>

def duration_to_secs(duration):
    duration_format = {
        'S': ['(\d+)S', 1], 
        'M': ['(\d+)M', 60], 
        'H': ['(\d+)H', 3600]
    }

    total_seconds = 0

    for _,v in duration_format.items():
        pattern = re.compile(r'{}'.format(v[0]))

        result =  pattern.findall(str(duration))

        if (len(result)) > 0:
            number =  result[0]
            total_seconds = total_seconds + (int(number) * v[1])

    return total_seconds

def get_api_key(key, response):
    try:
        if key == 'duration':
            return response['items'][0]['contentDetails']['duration']

        elif key == 'commentCount':
            return response['items'][0]['statistics']['commentCount']

        elif key == 'dislikeCount':
            return response['items'][0]['statistics']['dislikeCount']

        elif key == 'favoriteCount':
            return response['items'][0]['statistics']['favoriteCount']
        
        elif key == 'likeCount':
            return response['items'][0]['statistics']['likeCount']
        
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
    parts = "contentDetails,statistics"

    source_csv = '../../../resources/datasets/USvideos.csv'
    output_csv = '../../../resources/datasets/USvideos_duration.csv'
    partial_csv = '../../../resources/datasets/partial/partial.csv'

    restart_list = []

    if partial == True:
        reader = csv.DictReader(open(partial_csv))
        restart_list = [row['video_id'] for row in reader]

    youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey = DEVELOPER_KEY)

    df = pd.read_csv(source_csv)
    record = {}

    with open(file=output_csv, mode='w', newline='') as output_df:
        field_names = ["video_id", "duration", "commentCount", "dislikeCount", "favoriteCount", "likeCount", "viewCount", "timestamp"]
        
        csv_writer = csv.DictWriter(output_df, fieldnames=field_names, delimiter=',')
        csv_writer.writeheader()

        for video_id in df['video_id'].unique():
            if video_id not in restart_list:
                record['video_id'] = video_id

                request = youtube.videos().list(part=parts, id=video_id)
                response = request.execute()

                if debug == True:
                    print(json.dumps(response, indent=4, sort_keys=True)) 

                if (response['pageInfo']['totalResults']) > 0:
                    record['duration'] = duration_to_secs(get_api_key('duration', response))
                    record['commentCount'] = get_api_key('commentCount', response)
                    record['dislikeCount'] = get_api_key('dislikeCount', response)
                    record['favoriteCount'] = get_api_key('favoriteCount', response)
                    record['likeCount'] = get_api_key('likeCount', response)
                    record['viewCount'] = get_api_key('viewCount', response)                
                else:
                    record['duration'] = 0
                    record['commentCount'] = 0
                    record['dislikeCount'] = 0
                    record['favoriteCount'] = 0
                    record['likeCount'] = 0
                    record['viewCount'] = 0
                
                record['timestamp'] = str(datetime.datetime.now())

                csv_writer.writerow(record)
                time.sleep(sleep)
            else:
                print (f"Video {video_id} already in dataset store. Skipping..")

    print ("Process completed without errors")

if __name__ == "__main__":
    main(debug=False, partial=False) 
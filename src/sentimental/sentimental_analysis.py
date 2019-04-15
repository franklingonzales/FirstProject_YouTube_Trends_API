import pandas as pd
import csv
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 

def sentiment_scores(sentence):
    
    result = {}
    sentiment = SentimentIntensityAnalyzer()   
    sentiment_dict = sentiment.polarity_scores(sentence) 

    result['negative'] = sentiment_dict['neg']*100
    result['neutral'] = sentiment_dict['neu']*100
    result['positive'] = sentiment_dict['pos']*100
    
    if sentiment_dict['compound'] >= 0.05 :
        result['rate'] = "Positive"
  
    elif sentiment_dict['compound'] <= - 0.05 : 
        result['rate'] = "Negative"

    else :
        result['rate'] = "Neutral"

    return result

def main():
    source_csv = '../../resources/datasets/USvideos.csv'
    output_csv = '../../resources/datasets/US_sentimental.csv'

    df = pd.read_csv(source_csv)
    record = {}

    with open(file=output_csv, mode='w', newline='', encoding='utf-8') as output_df:
            field_names = ["video_id", "title_negative", "title_neutral", "title_positive", "title_rate", "tags_negative", "tags_neutral", "tags_positive", "tags_rate"]
            
            csv_writer = csv.DictWriter(output_df, fieldnames=field_names, delimiter=',')
            csv_writer.writeheader()

            for row in df[['video_id', 'title', 'tags']].groupby(by='video_id',as_index=False).first().iterrows():
                record['video_id'] = row[1]['video_id']

                sentiment = sentiment_scores(row[1]['title'])

                record['title_negative'] = sentiment['negative']
                record['title_neutral'] = sentiment['neutral']
                record['title_positive'] = sentiment['positive']
                record['title_rate'] = sentiment['rate']

                tags = row[1]['tags']
                sentiment = sentiment_scores(re.sub('[^A-Za-z]+', ' ', ' '.join(tags.split('|'))))

                record['tags_negative'] = sentiment['negative']
                record['tags_neutral'] = sentiment['neutral']
                record['tags_positive'] = sentiment['positive']
                record['tags_rate'] = sentiment['rate']

                csv_writer.writerow(record)

    print ("Process completed without errors")


if __name__ == "__main__":
    main() 

from datetime import datetime
import calendar
import pandas as pd
from tqdm import tqdm
import random

parties = [
    'platforma_org', 'Nowoczesna', 'Zieloni', 'inicjatywaPL', 
    'KONFEDERACJA_', 'RuchNarodowy', 'Partia_KORWiN', 
    'nowePSL', 'KUKIZ15',
    '__Lewica', 'partiarazem',
    'Porozumienie__', 'SolidarnaPL', 'pisorgpl'
]

files_dir = './home/data/'
save_dir = './home/data/to_vis/'


for i in tqdm(range(len(parties))):
    party = parties[i]

    df_profile = pd.read_csv(''.join([
        files_dir, party, '_profile.csv'
    ]))
    df_mentions = pd.read_csv(''.join([
        files_dir, party, '_mentions.csv'
    ]))

    df_profile['retweet'] = df_profile['retweet'].map({
        True: 'Retweet',
        False: 'Tweet'
    })
    df_mentions['retweet'] = df_mentions['retweet'].map({
        True: 'Retweet',
        False: 'Tweet'
    })

# to fill no data with zeros
def get_rand_id():
    return random.randint(100000, 600000) + random.randint(100000, 600000) + random.randint(100000, 600000)
def fill(df, col1, col1_values,  col2):
    for v in col1_values:
        if(len(df[df[col1]==v][col2]) == 0):
            df = df.append(pd.Series({
                col1: v,
                col2: 0
            }, name=get_rand_id()))
    df = df.fillna('s')
    return df
days_l = []
for i in range(16,32):
    days_l.append('2020-09-'+str(i))
for i in range(1,10):
    days_l.append('2020-10-0'+str(i))
for i in range(10,17):
    days_l.append('2020-10-'+str(i))
hours_l = [i for i in range(0,24)]
week_days_l = [i for i in range(0,7)]


for i in tqdm(range(len(parties))):
    party = parties[i]

    df_profile = pd.read_csv(''.join([
        files_dir, party, '_profile.csv'
    ]))
    df_mentions = pd.read_csv(''.join([
        files_dir, party, '_mentions.csv'
    ]))

    df_profile['retweet'] = df_profile['retweet'].map({
        True: 'Retweet',
        False: 'Tweet'
    })
    df_mentions['retweet'] = df_mentions['retweet'].map({
        True: 'Retweet',
        False: 'Tweet'
    })


    # tweets and retweets number
    data = df_profile[['id', 'date', 'retweet']].groupby(['retweet', 'date']).count().reset_index(inplace=False).copy()
    data_tweets = data[data['retweet']=='Tweet'].copy()
    data_tweets = fill(data_tweets.copy(), 'date', days_l, 'id')
    data_retweets = data[data['retweet']=='Retweet'].copy()
    data_retweets = fill(data_retweets.copy(), 'date', days_l, 'id')
    out1 = data_tweets.to_json()
    with open(''.join([save_dir, party,'_tweets_num.json']), 'w') as f:
        f.write(out1)
    out2 = data_retweets.to_json()
    with open(''.join([save_dir, party,'_posted_retweets_num.json']), 'w') as f:
        f.write(out2)


    # reactions number
    data = df_profile[df_profile['retweet']=='Tweet']
    data = data[['date', 'likes_count', 'replies_count', 'retweets_count']].groupby(['date']).sum().reset_index(inplace=False)
    data = data.rename(columns={
            'likes_count': 'likes',
            'replies_count': 'replies',
            'retweets_count': 'retweets'
    })
    data = data.copy()
    data = fill(data, 'date', days_l, 'likes')
    data = fill(data, 'date', days_l, 'replies')
    data = fill(data, 'date', days_l, 'retweets')
    out3 = data[['date', 'likes']].to_json()
    with open(''.join([save_dir, party, '_likes_num.json']), 'w') as f:
        f.write(out3)
    out4 = data[['date', 'replies']].to_json()
    with open(''.join([save_dir, party, '_replies_num.json']), 'w') as f:
        f.write(out4)
    out5 = data[['date', 'retweets']].to_json()
    with open(''.join([save_dir, party, '_retweets_num.json']), 'w') as f:
        f.write(out5)


    # mentions number
    data = df_mentions[['date','id']].groupby('date').count().reset_index(inplace=False)
    data = fill(data.copy(), 'date', days_l, 'id')
    data.to_json(''.join([
        save_dir, party, '_mentions_num.json'
    ]))


    # Posts polarity in time
    data = df_profile[['polarity', 'date', 'retweet']].groupby(['retweet', 'date']).mean().reset_index(inplace=False)
    fill(data[data['retweet']=='Tweet'][['date', 'polarity']].copy(), 'date', days_l, 'polarity').to_json(''.join([
        save_dir, party, '_tweets_polarity.json'
    ]))
    fill(data[data['retweet']=='Retweet'][['date', 'polarity']].copy(), 'date', days_l, 'polarity').to_json(''.join([
        save_dir, party, '_retweets_polarity.json'
    ]))


    # Mentions polarity
    data = df_mentions[['polarity', 'date']].groupby('date').mean().reset_index(inplace=False)
    fill(data.copy(), 'date', days_l, 'polarity').to_json(''.join([
        save_dir, party, '_mentions_polarity.json'
    ]))


    # Posts in day scope
    data = df_profile[['id', 'time', 'retweet']]
    data['hour'] = data.apply(lambda x: int(x['time'][0:2]), axis=1)
    data = data.groupby(['retweet', 'hour']).count().reset_index(inplace=False)
    fill(data[data['retweet']=='Tweet'][['hour', 'id']].copy(), 'hour', hours_l, 'id').to_json(''.join([
        save_dir, party, '_tweets_day.json'
    ]))
    fill(data[data['retweet']=='Retweet'][['hour', 'id']].copy(), 'hour', hours_l, 'id').to_json(''.join([
        save_dir, party, '_retweets_day.json'
    ]))


    # Posts in week scope
    data = df_profile[['id', 'date', 'retweet']]
    data['week_day'] = data.apply(lambda x: datetime.strptime(x['date'], '%Y-%m-%d').weekday(), axis=1)
    data = data.groupby(['retweet', 'week_day']).count().reset_index(inplace=False)
    fill(data[data['retweet']=='Tweet'][['week_day', 'id']].copy(), 'week_day', week_days_l, 'id').to_json(''.join([
        save_dir, party, '_tweets_week.json'
    ]))
    fill(data[data['retweet']=='Retweet'][['week_day', 'id']].copy(), 'week_day', week_days_l, 'id').to_json(''.join([
        save_dir, party, '_retweets_week.json'
    ]))
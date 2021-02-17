import pandas as pd
import twint
import nest_asyncio
nest_asyncio.apply()

parties = [
    'platforma_org', 'Nowoczesna', 'Zieloni', 'inicjatywaPL', 
    'KONFEDERACJA_', 'RuchNarodowy', 'Partia_KORWiN', 
    'nowePSL', 'KUKIZ15',
    '__Lewica', 'partiarazem',
    'Porozumienie__', 'SolidarnaPL', 'pisorgpl'
]

since = '2020-09-16'

save_dir = './home/scrapped_data/'

for party in parties:

    #scrap profile
    c = twint.Config()
    c.Username = party
    c.Retweets = True
    c.Store_csv = True
    c.Output = ''.join([save_dir, party, '_profile.csv'])
    c.Since = since
    twint.run.Profile(c)

    #scrap mentions
    c = twint.Config()
    c.Search = '@'+party
    c.Store_csv = True
    c.Output = ''.join([save_dir, party, '_mentions.csv'])
    c.Since = since
    twint.run.Search(c)
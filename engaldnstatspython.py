import pandas as pd
import sqlite3
import logging

df = pd.read_csv('englandstats.csv')

con = sqlite3.connect('englandstats.db')

df

new_df = df['Nationality'] = 'Germany'

df

new_df = df.to_sql('englandstats', con, if_exists='replace')
print(new_df)

logging.basicConfig(
    filename='loggengland.txt',
    format='[%(asctime)s][%(levelname)s]%(message)s',
    level=logging.DEBUG
)

logger = logging.getLogger(__name__)
logger.debug('AjAj')
logger.info('Tjena')
logger.warning('Akta dig för detta')
logger.critical('Någon hackar')

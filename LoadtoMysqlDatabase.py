import warnings
warnings.filterwarnings('ignore')

from sqlalchemy import  create_engine
import pandas as pd

engine = create_engine("mysql+mysqldb://root:1234@localhost:3306/koora_data") # {root}:{password}@host:port/{database name}

#Establish a connection
conn = engine.connect()

#Read data from CSV into a Pandas DataFrame
data = pd.read_csv("LastData.csv")

#Write DataFrame to a SQL table
data.to_sql('KOORA', engine, index=False, if_exists='replace')

#Close Connection
conn.close()

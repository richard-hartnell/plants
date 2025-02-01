import datetime
from datetime import date
import json
import sqlite3
import pandas as pd

plant_types = []
plants = []
year = datetime.datetime.now().year
first_frost = datetime.date(year, 10, 22)
last_frost = datetime.date(year, 4, 15)

conn = sqlite3.connect('nanofarm.db')
df = pd.read_sql('SELECT * FROM plants', conn)
print(df)

class Plant:
    def __init__(self): # , name, root_length, cold, hot, maturity_age, direct_sow
        pass

    def when_to_sow(self):
        if self.cold:       
            self.sow1_start = date(year, 2, 1)  # Spring planting
            self.sow1_end = date(0000, 5, 1)
        if self.hot:
            self.sow2_start = date(year, 7, 15)  # Fall planting
            self.sow2_end = date(year, 8, 15)
        else:
            self.sow1_start = date(year,5, 1)
            self.sow1_end = date(year, 7, 1)
            self.sow2_start = None
            self.sow2_end = None

def generate_plant_class(name, base_class, attrs):
    # Create a new class that inherits from base_class with additional attributes
    return type(name, (base_class,), attrs)

for row in df.itertuples():

    _plant_attrs = {
        'plant_type': row.name,
        'root_distance': row.root_distance,
        'cold': row.cold,
        'hot': row.hot,
        'days_to_mature': row.days_to_mature,
        'direct_sow': row.direct_sow
    }

    if row.name in plant_types:
        pass
    else:
        plant_types.append(row.name)
        generate_plant_class(row.name, Plant, _plant_attrs)
    
    # how do I generate the object name from the varietal field here?

conn.close()

print (plant_types)
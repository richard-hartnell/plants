import datetime
from datetime import date
import json
import sqlite3
# import pandas as pd

plant_types = []
plants = []
year = datetime.datetime.now().year
first_frost = datetime.date(year, 10, 22)
last_frost = datetime.date(year, 4, 15)

# conn = sqlite3.connect('nanofarm.db')
# df = pd.read_sql('SELECT * FROM plants', conn)

class Plant:
    def __init__(self): # , name, root_length, early, late, maturity_age, direct_sow
        pass

    def when_to_sow(self):
        if self.early:       
            self.sow1_start = date(year, 2, 1)  # Spring planting
            self.sow1_end = date(0000, 5, 1)
        if self.late:
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

##TESTING ZONE

# subclass_attrs = {
#     'plant_type': 'Bean',
#     'root_length': 6,
#     'early': 0,
#     'late': 0,
#     'maturity_age': 80,
#     'direct_sow': 0
# }

# Bean = generate_plant_class('Bean', Plant, subclass_attrs)
# Lettuce = generate_plant_class('Lettuce,', Plant, subclass_attrs)

# dragon_tongue = Bean()

# print(dragon_tongue.plant_type)
# print(dragon_tongue.root_length)
# dragon_tongue.when_to_sow()

# print(dragon_tongue.sow1_start)
# print(dragon_tongue.sow2_start)

for row in df.itertuples():

    _plant_attrs = {
        'plant_type': row.name,
        'root_distance': row.root_distance,
        'early': row.early,
        'late': row.late,
        'days_to_mature': row.days_to_mature,
        'direct_sow': row.direct_sow
    }

    if row.name in plant_types:
        pass
    else:
        plant_types += row.name
        generate_plant_class(row.name, Plant, _plant_attrs)
    
    # how do I generate the object name from the varietal field here?

conn.close()
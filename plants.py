import datetime
from datetime import date
import json
import sqlite3
import pandas as pd

plant_types = []
plants = []
plots = []
year = datetime.datetime.now().year
first_frost = datetime.date(year, 10, 22)
last_frost = datetime.date(year, 4, 15)

conn = sqlite3.connect('nanofarm.db')
df_types = pd.read_sql('SELECT * FROM plant_types', conn)
print(df_types)

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

class Plot:
    def __init__(self): # , name, root_length, cold, hot, maturity_age, direct_sow
        self.hot_plants = []
        self.cold_plants = []
        self.max_root_length = 0
        plots.append(self)
        pass

    def add_plant(self, plant):
        if plant.cold:
            self.cold_plants.append(plant)
        else:
            self.hot_plants.append(plant)

def generate_plant_class(name, base_class, attrs):
    # Create a new class that inherits from base_class with additional attributes
    return type(name, (base_class,), attrs)

def plot_plants():
    pass

for row in df_types.itertuples():

    _plant_attrs = {
        'plant_type': row.plant_type, #need to change this in db.
        'root_distance': row.root_distance,
        'cold': row.cold,
        'hot': row.hot,
        'days_to_mature': row.days_to_mature,
        'direct_sow': row.direct_sow,
        'varietal': row.varietal,
        'friends': row.friends,
        'foes': row.foes,
        'allium': row.allium,
        'brassica': row.brassica,
    }

    if row.plant_type in plant_types: #need to change "name" in db to "plant_type"
        pass
    else:
        plant_types.append(generate_plant_class(row.plant_type, Plant, _plant_attrs))
    
conn.close()

for plant in plant_types:
    print(plant.plant_type)

#OO
# on run, load all plants from the database
# check for any plants in the db that aren't in a plot.
# assign them automatically if poss.
# # use the comparison planting sheet in a function like workshop_scheduler
# if not, ask user to assign them
# then, calc max root length for each plot
# apply calculation from PLANTS sheet for hex size & number of hexes
# ...
# make plants
import datetime
import json
import sqlite3
import pandas as pd

year = datetime.datetime.now().year
first_frost = datetime.date(year, 10, 22)
last_frost = datetime.date(year, 4, 15)

conn = sqlite3.connect('nanofarm.db')
df = pd.read_sql('SELECT * FROM plants', conn)

class Plant:
    def __init__(self, name, root_length, early, late, maturity_age, direct_sow):
        self.name = name
        self.root_length = root_length
        self.early = early
        self.late = late
        self.maturity_age = maturity_age
        self.direct_sow = direct_sow


# here is where you need to create the plant subclasses from "plant" above.

def generate_plant(name, base_class, attrs):
    # Create a new class that inherits from base_class with additional attributes
    return type(name, (base_class,), attrs)


#example

subclass_attrs = {
    # example method
    'speak': lambda self: "Bark",
    # New attribute
    'legs': 4
    # revise attribute?
}

Bean = generate_plant('Bean', Plant, subclass_attrs)


# experimental subclassing code ends



# Create a dictionary of plants
for row in df.itertuples():


    plant = {
        'name': row.name,
        'root_distance': row.root_distance,
        'hot': row.hot,
        'cold': row.cold,
        'days_to_mature': row.days_to_mature,
        'direct_sow': row.direct_sow
    }
    print(plant['cold'])

    # def __str__(self):
    #     return f"{self.name} ({self.species})"
    
    def when_to_sow(self, early, late):
        if self.early:       
            sow1_start = date(year, 2, 1)  # Spring planting
            sow1_end = date(0000, 5, 1)
        if self.late:
            sow2_start = date(year, 7, 15)  # Fall planting
            sow2_end = date(year, 8, 15)
        else:
            sow1_start = date(year,5, 1)
            sow1_end = date(year, 7, 1)

    def plot(self):
        # run the comparison of plant's companions
        pass

conn.close()
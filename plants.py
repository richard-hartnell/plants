import datetime
import json
import sqlite3
import pandas as pd

year = datetime.datetime.now().year
first_frost = datetime.date(year, 10, 22)
last_frost = datetime.date(year, 4, 15)

conn = sqlite3.connect('nanofarm.db')
df = pd.read_sql('SELECT * FROM plants', conn)
print (df)

# Create a dictionary of plants
for row in df.itertuples():
    plant = {
        'name': row.name,
        'root_length': row.root_distance,
    }
    print(plant['name'])

class Plant:
    def __init__(self, name, root_length, number_per_hex, early, late, maturity_age, direct_sow):
        self.name = name
        self.root_length = root_length
        self.early = early
        self.late = late
        self.maturity_age = maturity_age
        self.number_per_hex = number_per_hex
        self.direct_sow = direct_sow

    def __str__(self):
        return f"{self.name} ({self.species})"
    
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
    
# class Bean(Plant):
#     def __init__(self, name, varietal=None):
#         # Default values for beans
#         root_length = 6  # inches
#         number_per_hex = None
#         early = False
#         late = False
#         maturity_age = 60  # days
#         direct_sow = False
        
#         super().__init__(
#             name=name,
#             varietal=varietal,
#             root_length=root_length,
#             number_per_hex=number_per_hex,
#             early=early,
#             late=late,
#             maturity_age=maturity_age,
#             direct_sow=direct_sow,
#             self.when_to_sow(self, early, late)
#         )

# class Beet(Plant):
#     def __init__(self, name, varietal=None):
#         # Default values for beets
#         root_length = 6  # inches
#         number_per_hex = 9
#         early = True
#         late = False
#         maturity_age = 60  # days
#         direct_sow = True
        
#         super().__init__(
#             name=name,
#             varietal=varietal,
#             root_length=root_length,
#             number_per_hex=number_per_hex,
#             early=early,
#             late=late,
#             maturity_age=maturity_age,
#             direct_sow=direct_sow,
#             self.when_to_sow(early, late)
#         )

# class Broccoli(Plant):
#     def __init__(self, name, varietal=None):
#         # Default values for broccoli
#         root_length = 12  # inches
#         number_per_hex = 1
#         early = True
#         late = False
#         maturity_age = 60  # days
#         direct_sow = False
        
#         super().__init__(
#             name=name,
#             varietal=varietal,
#             root_length=root_length,
#             number_per_hex=number_per_hex,
#             early=early,
#             late=late,
#             maturity_age=maturity_age,
#             direct_sow=direct_sow,
#             self.when_to_sow(early, late)
#         )

conn.close()
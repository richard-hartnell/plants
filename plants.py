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
cursor = conn.cursor()

df_plant_types = pd.read_sql('SELECT * FROM plant_types', conn)
df_plots = pd.read_sql('SELECT * FROM plots', conn)
df_this_year = pd.read_sql('SELECT * FROM this_year', conn)

def plant_this_plant(_id, _varietal, _plant_type, _plot):
    cursor.execute('''
                INSERT INTO 'this_year' (id, varietal, plant_type, plot)
                VALUES (?, ?, ?, ?)
                ''', (_id, _varietal, _plant_type, _plot))
    conn.commit()
    pass

def update_this_plant(_id, _varietal, _plant_type, _plot):
    cursor.execute('''
                UPDATE 'this_year'
                SET varietal = ?, plant_type = ?, plot = ?
                WHERE id = ?
                ''', (_varietal, _plant_type, _plot, _id))
    conn.commit()
    pass

#TODO: make this add the plot to the plant (plant can be added to plot with Plot.plant(plant))
def plot_plant(plant):
    cursor.execute('''
                INSERT INTO 'this_year' (id, varietal, plant_type, plot)
                VALUES (?, ?, ?, ?)
                ''', (plant.id, plant., _plant_type, _plot))
    conn.commit()
    pass

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
    # # # so technically, this should just be a function that assigns plants to plots,
    # # # not the function that decides which plants go into plots.

    # # Assign plants to plots
    # first, assign biggest plants (root length >14 in)
    # check_compatibility(plant)
    # display available plots to user
    ## make sure they include all other plants so far.
    end_plot = input("Which plot would you place this plant in?")

    # then add the plant to the prompted plot
    pass

def check_compatibility(plant):
    _friendly_plots = []
    for plot in plots:
        for _plant in plot:
            if _plant.name in plant.friends:
                print (plot.name)
    print(_friendly_plots)
    
        
    return False

def fetch_plant_types():    
    for row in df_plant_types.itertuples():

        _plant_attrs = {
            'plant_type': row.plant_type,
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

        if row.plant_type in plant_types:
            pass
        else:
            plant_types.append(generate_plant_class(row.plant_type, Plant, _plant_attrs))

def fetch_plots():
    for row in df_plots.itertuples():
        _plot_attrs = {
            'plot_name': row.plot_name,
            'area': row.area,
            'root_max': row.root_max,
        }
        if row.plot_name in plots:
            pass
        else:
            plots.append(generate_plant_class(row.plot_name, Plot, _plot_attrs))

conn.close()

#OO
# on run, load all plants and plots from the database. DONE
# load this year's plants (this_year). DONE
# append all plant_type info to each plant.
# check for any plants in the db that aren't in a plot.
def check_unplotted_plants:
    for plant in plants:
        if not plant.plot:

# assign them automatically if possible
# # use the comparison planting sheet in a function like workshop_scheduler
# if not, ask user to assign them
# then, calc max root length for each plot
# apply calculation from PLANTS sheet for hex size & number of hexes
# ...
# make plants

#OO 2
# # read in plots.
# read in plant types.

# # # check for companion planting compatibility
# # start with the big plants.
# if there's a different big plant type in a plot, move to a different plot.
# this means you should have a limit of three big hot plants and three (six?) big cold plants.
# # interplant the smaller plants (root length ~1/2 the big L)
# if there's a friend in the plot, add 1 point.
# if there's a foe in the plot, subtract 3 points.
# # keep in mind cold/hot planting.
# make cold plants ignore hot plants and vice versa.
# # on exit, rewrite everything to DB.

# # is it easier to just make the internal DB and then compare the internal DB with the static one?
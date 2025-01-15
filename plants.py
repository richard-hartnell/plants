import datetime
import json

class Plant:
    def __init__(self, name, varietal='', root_length, number_per_hex, early, late, maturity_age, sow1_start, sow2_start='', sow1_end, sow2_end=''):
        self.name = name
        self.varietal = varietal
        self.root_length = root_length
        self.early = early
        self.late = late
        self.maturity_age = maturity_age
        self.number_per_hex = number_per_hex
        self.sow1_start = sow1_start
        self.sow1_end = sow1_end
        self.sow2_start = sow2_start
        self.sow2_end = sow2_end
        self.season_length = (sow1_end - sow1_start) + (sow2_end - sow2_start)


    def water(self):
        self.last_watered_on = datetime.datetime.now()

    def __str__(self):
        return f"{self.name} ({self.species})"
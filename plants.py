import datetime
import json

year = datetime.now().year

first_frost = datetime.date(year, 10, 22)
last_frost = datetime.date(year, 4, 15)

class Plant:
    def __init__(self, name, root_length, number_per_hex, early, late, maturity_age, sow1_start, sow1_end, direct_sow, sow2_start=None, sow2_end=None, varietal=None):
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
        self.direct_sow = direct_sow
        self.season_length = (sow1_end - sow1_start).days + (sow2_end - sow2_start).days

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
    
class Bean(Plant):
    def __init__(self, name, varietal=None):
        # Default values for beans
        root_length = 6  # inches
        number_per_hex = None
        early = False
        late = False
        maturity_age = 60  # days
        direct_sow = False
        
        super().__init__(
            name=name,
            varietal=varietal,
            root_length=root_length,
            number_per_hex=number_per_hex,
            early=early,
            late=late,
            maturity_age=maturity_age,
            direct_sow=direct_sow
            self.when_to_sow(early, late)
        )
        self.species = "Phaseolus vulgaris"
        self.climbing = True  # Bean-specific attribute
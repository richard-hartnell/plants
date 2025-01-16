# plants
a garden scripting station.

## The new version of the PLANTS sheet
Now with more dynamic behavior. Designed so I can quit Taskade.

### TODO LIST

- incorporate dates.
- handle a table of plants and a table of plots.
- create a garden plan based on companion planting and rotation
- populate Google Calendar events with:
    - plantings
    - harvest dates
    - pruning
    - weeding tasks
    - hardening tasks
    - winterizing tasks
    - long-term plans

### The plan:

- bulid out the database from the PLANTS sheet
- build out the calendar functionality (add calendar events)
- create something like workshop_scheduler to plot plants?
- add a verison of bcg-emailer for extra harrassment
- integrate that companion planting sheet where each object can be mutually referred to

### What's it do?

-Reads in database of plants from SQL

-Automatically detects companion planting compatibilities/incompatibilities

-Sorts cold plants, warm plants into companion planting categories (three sisters as alpha test)

-Measures max root length of each companion planting group

-Determines number of plantings of each plant and calculates seeds required

-Schedules plantings for each biweekly planting sesh

-Sends emails
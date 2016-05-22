import csv
import json
import pprint

from tinydb import TinyDB, Query # required module, install with: pip install tinydb

DB = TinyDB('db.json')

FILEPATH = 'sf_popos.csv'


# only run once to load and initialize DB with contacts.json; 
# else DB will have duplicate entries
def load_DB(FILEPATH):
    """
    Loads TinyDB with sf_popos.csv data, returns searchable db.json

    """

    with open(FILEPATH, 'r') as fn:    
        data = csv.DictReader(fn)

        for row in data:
            # element = OrderedDict(element)
            pprint.pprint(row)

            DB.insert(row)

load_DB(FILEPATH)
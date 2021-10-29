import random

inventory = []
itemlist = []

items=["sword","bow","arrow","bomb","shield"]
attributes=["wood","metal","fire","poison"]

for Items in items:
        for Attributes in attributes:
             itemlist.append(Attributes+" "+Items)


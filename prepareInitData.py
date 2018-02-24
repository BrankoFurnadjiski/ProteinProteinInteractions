"""
This file does the pre-processing of the 9606.protein.links file.
"""
import gzip
from entry import Entry
import pandas as pd
import time
import csv

flag = True

# Contains all PPIs. The key is protein1-protein2, the value is the entire row of data.
entries = dict()
 
print("(" + time.strftime("%c") + ")  Reading Protein Links file...")

# Filling entries dictionary
with gzip.open('../data/9606.protein.links.detailed.v10.5.txt.gz','r') as fin:        
    for line in fin:
        if flag:
            flag = False
            continue
        line = line.decode('ascii')
        line = line[:-1]
        parts = line.split(" ")
        entry = Entry(parts[0], parts[1], int(parts[2]), int(parts[3]), int(parts[4]), int(parts[5]), int(parts[6]), int(parts[7]), int(parts[8]), int(parts[9]))
        entries[entry.getLinkName()] = entry
 
 
print("(" + time.strftime("%c") + ")  Writing into HumanPPI, HumanPPI700 & HumanPPI900...")

# Writing into:
HumanPPI = open("../data/HumanPPI.txt", "w")
HumanPPI700 = open("../data/HumanPPI700.txt", "w")
HumanPPI900 = open("../data/HumanPPI900.txt", "w")

# Writing data into HumanPPI, HumanPPI700, HumanPPI900
for key in entries.keys():
    HumanPPI.write(str(entries[key]))
    HumanPPI.write('\n')
    if entries[key].getCombinedScore() >= 900:
        HumanPPI900.write(str(entries[key]))
        HumanPPI900.write('\n')
        HumanPPI700.write(str(entries[key]))
        HumanPPI700.write('\n')
    elif entries[key].getCombinedScore() >= 700:
        HumanPPI700.write(str(entries[key]))
        HumanPPI700.write('\n')

HumanPPI.close()
HumanPPI700.close()
HumanPPI900.close()

print("(" + time.strftime("%c") + ")  You done now")
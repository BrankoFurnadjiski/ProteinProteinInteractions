"""
This file connects string-db protenins with GO annotations according to GO Consortium
"""
import gzip
import time

# Counter for skipping rows
counter = 1

# Flag for skipping first row
flag = True

# Dictionary for mapping from stringID to uniprotIDs
stringMapping = dict()

# Dictionary for mapping from uniprotID to GO annotation
uniMapping = dict()

# Reading from:
GOAHuman = open("../data/goa_human_164.gaf", "r")
HumanPPI700Links = open("../data/HumanPPI700_Links.txt", "r")
HumanPPI900Links = open("../data/HumanPPI900_Links.txt", "r")

# Writing into:
HumanPPI700GO = open("../data/HumanPPI700_GO_v2.txt", "w")
HumanPPI900GO = open("../data/HumanPPI900_GO_v2.txt", "w")

# Reading from these to create child-parent relationships:
BPGOfull = open("../data/BPGOfull.txt", "r")
MFGOfull = open("../data/MFGOfull.txt", "r")
CCGOfull = open("../data/CCGOfull.txt", "r")

print("(" + time.strftime("%c") + ")  Reading Uniprot...")

# Filling stringMapping dictionary 
with gzip.open('../data/9606_reviewed_uniprot_2_string.04_2015.tsv.gz','r') as fin:        
	for line in fin:
		if flag:
			flag = False
			continue
		line = line.decode('ascii')
		line = line[:-1]
		parts = line.split("\t") 
		stringId = parts[0] + "." + parts[2]
		fullUniprotId = parts[1]
		uniprotId = fullUniprotId.split("|")[0]
		stringMapping[stringId] = uniprotId


print("(" + time.strftime("%c") + ")  Reading GOA...")		

# Filling uniMapping dictionary
for line in GOAHuman:
	if counter <= 12:
		counter += 1
		continue
	parts = line.split("\t")
	uniprotId = parts[1]
	goId = parts[4]

	if uniprotId not in uniMapping:
		uniMapping[uniprotId] = set()

	uniMapping[uniprotId].add(goId)

print("(" + time.strftime("%c") + ")  Writing into HumanPPI700_GO_v2...")

# Writing GO annotations for proteins in HumanPPI700 into HumanPPI700_GO 
for line in HumanPPI700Links:
	parts = line.split(" -> ")
	stringId = parts[0]

	if stringId not in stringMapping:
		continue

	uniprotId = stringMapping[stringId]

	if uniprotId not in uniMapping:
		continue
	else:
		goTerms = uniMapping[uniprotId]

		for go in goTerms:
			HumanPPI700GO.write(stringId + "\t" + uniprotId + "\t" + go + "\t\n")



print("(" + time.strftime("%c") + ")  Writing into HumanPPI900_GO_v2...")

# Writing GO annotations for proteins in HumanPPI700 into HumanPPI700_GO 
for line in HumanPPI900Links:
	parts = line.split(" -> ")
	stringId = parts[0]

	if stringId not in stringMapping:
		continue

	uniprotId = stringMapping[stringId]

	if uniprotId not in uniMapping:
		continue
	else:
		goTerms = uniMapping[uniprotId]

		for go in goTerms:
			HumanPPI900GO.write(stringId + "\t" + uniprotId + "\t" + go + "\t\n")


GOAHuman.close()
HumanPPI700Links.close()
HumanPPI900Links.close()

HumanPPI700GO.close()
HumanPPI900GO.close()

BPGOfull.close()
MFGOfull.close()
CCGOfull.close()

print("(" + time.strftime("%c") + ")  You done now!!!")
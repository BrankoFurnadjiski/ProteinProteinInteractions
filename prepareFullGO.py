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
HumanPPI700GO = open("../data/HumanPPI700_GO.txt", "w")
HumanPPI900GO = open("../data/HumanPPI900_GO.txt", "w")

# Reading from these to create child-parent relationships:
BPGOfull = open("../data/BPGOfull.txt", "r")
MFGOfull = open("../data/MFGOfull.txt", "r")
CCGOfull = open("../data/CCGOfull.txt", "r")

# Stores child-parent relationships for GO annotations
childParentRelationship = dict()

print("(" + time.strftime("%c") + ")  Filling childParentRelationship dictionary...")

for line in BPGOfull:
		line = line[:-1]
		parts = line.split(" ")
		child = parts[0]
		relationship = parts[1]
		parent = parts[2]
		if relationship != "is_a":
			continue
		childParentRelationship[child] = parent

for line in MFGOfull:
		line = line[:-1]
		parts = line.split(" ")
		child = parts[0]
		relationship = parts[1]
		parent = parts[2]
		if relationship != "is_a":
			continue
		childParentRelationship[child] = parent

for line in CCGOfull:
		line = line[:-1]
		parts = line.split(" ")
		child = parts[0]
		relationship = parts[1]
		parent = parts[2]
		if relationship != "is_a":
			continue
		childParentRelationship[child] = parent


def allParentsOf(goId):
	allParentAnnotations = []

	while goId in childParentRelationship:
		allParentAnnotations.append(goId)
		goId = childParentRelationship[goId]

		if goId not in childParentRelationship:
			allParentAnnotations.append(goId)

	return allParentAnnotations


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
	evidence = parts[6]
	goId = parts[4]

	# Filter out the rows with IEA evidence
	if evidence == 'IEA':
		continue

	if uniprotId not in uniMapping:
		uniMapping[uniprotId] = set()

	parents = allParentsOf(goId)
	for p in parents:
		uniMapping[uniprotId].add(p)



print("(" + time.strftime("%c") + ")  Writing into HumanPPI700_GO...")

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



print("(" + time.strftime("%c") + ")  Writing into HumanPPI900_GO...")

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
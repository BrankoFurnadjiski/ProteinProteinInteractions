"""
This file creates the neighborhood matrix, optimized using dictionary instead of sparse matrix.
"""

from proteinWrapper import ProteinWrapper
import time

# Contains all proteins as a key. The value is a list of ProteinWrapper's that the key interacts with.
interactions = dict()

# Redaing from:
HumanPPI = open("../data/HumanPPI.txt", "r")
HumanPPI700 = open("../data/HumanPPI700.txt", "r")
HumanPPI900 = open("../data/HumanPPI900.txt", "r")

# Writing into:
HumanPPILinks = open("../data/HumanPPI_Links.txt", "w")
HumanPPI700Links = open("../data/HumanPPI700_Links.txt", "w")
HumanPPI900Links = open("../data/HumanPPI900_Links.txt", "w")


print("(" + time.strftime("%c") + ")  Reading HumanPPI...")

# Filling interactions dictionary for HumanPPI
for line in HumanPPI:
	parts = line.split(", ")
	protein1 = parts[0]
	protein2 = parts[1]
	weight = int(parts[9])

	if protein1 not in interactions.keys():
		interactions[protein1] = []

	interactions[protein1].append(ProteinWrapper(protein2, weight))

print("(" + time.strftime("%c") + ")  Writing into HumanPPI_Links...")

# Writing interactions dictionary into HumanPPILinks
for key in interactions.keys():
	links = interactions[key]
	HumanPPILinks.write(key + " -> ")
	for i in range(len(links)):
		HumanPPILinks.write(str(links[i]))
		if i != (len(links)-1):
			HumanPPILinks.write(", ")
	HumanPPILinks.write('\n')

print("(" + time.strftime("%c") + ")  Reading HumanPPI700...")

# Resetting dictionary 
interactions = dict()

# Filling interactions dictionary for HumanPPI700
for line in HumanPPI700:
	parts = line.split(", ")
	protein1 = parts[0]
	protein2 = parts[1]
	weight = int(parts[9])

	if protein1 not in interactions.keys():
		interactions[protein1] = []

	interactions[protein1].append(ProteinWrapper(protein2, weight))

print("(" + time.strftime("%c") + ")  Writing into HumanPPI700_Links...")

# Writing interactions dictionary into HumanPPI700Links
for key in interactions.keys():
	links = interactions[key]
	HumanPPI700Links.write(key + " -> ")
	for i in range(len(links)):
		HumanPPI700Links.write(str(links[i]))
		if i != (len(links)-1):
			HumanPPI700Links.write(", ")
	HumanPPI700Links.write('\n')


print("(" + time.strftime("%c") + ")  Reading HumanPPI900...")

# Resetting dictionary 
interactions = dict()

# Filling interactions dictionary for HumanPPI900
for line in HumanPPI900:
	parts = line.split(", ")
	protein1 = parts[0]
	protein2 = parts[1]
	weight = int(parts[9])

	if protein1 not in interactions.keys():
		interactions[protein1] = []

	interactions[protein1].append(ProteinWrapper(protein2, weight))

print("(" + time.strftime("%c") + ")  Writing into HumanPPI900_Links...")

# Writing interactions dictionary into HumanPPI900Links
for key in interactions.keys():
	links = interactions[key]
	HumanPPI900Links.write(key + " -> ")
	for i in range(len(links)):
		HumanPPI900Links.write(str(links[i]))
		if i != (len(links)-1):
			HumanPPI900Links.write(", ")
	HumanPPI900Links.write('\n')


HumanPPI.close()
HumanPPI700.close()
HumanPPI900.close()

HumanPPILinks.close()
HumanPPI700Links.close()
HumanPPI900Links.close()

print("(" + time.strftime("%c") + ")  You done now")
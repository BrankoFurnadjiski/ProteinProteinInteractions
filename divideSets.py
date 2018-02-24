"""
This file divides the files HumanPPI700GO and HumanPPi900GO into three sets according to fucntions MF, BP and CC
"""
import time

ccgoDict = dict()
bpgoDict = dict()
mfgoDict = dict()

# Reading from:
HumanPPI700GO = open("../data/HumanPPI700_GO.txt", "r")
HumanPPI900GO = open("../data/HumanPPI900_GO.txt", "r")
CCGOterms = open("../data/CCGOterms.txt", "r")
MFGOterms = open("../data/MFGOterms.txt", "r")
BPGOterms = open("../data/BPGOterms.txt", "r")

# Writing into:
HumanPPI700GOMF = open("../data/HumanPPI700_GO_MF.txt", "w")
HumanPPI900GOMF = open("../data/HumanPPI900_GO_MF.txt", "w")
HumanPPI700GOCC = open("../data/HumanPPI700_GO_CC.txt", "w")
HumanPPI900GOCC = open("../data/HumanPPI900_GO_CC.txt", "w")
HumanPPI700GOBP = open("../data/HumanPPI700_GO_BP.txt", "w")
HumanPPI900GOBP = open("../data/HumanPPI900_GO_BP.txt", "w")

print("(" + time.strftime("%c") + ")  Reading CCGOterms file...")

# Filling  CCGO dictionary 
for line in CCGOterms:
	ccgoDict[line[:-1]] = True

print("(" + time.strftime("%c") + ")  Reading MFGOterms file...")

# Filling  MFGO dictionary 
for line in MFGOterms:
	mfgoDict[line[:-1]] = True

print("(" + time.strftime("%c") + ")  Reading BPGOterms file...")

# Filling  BPGOterms dictionary 
for line in BPGOterms:
	bpgoDict[line[:-1]] = True


print("(" + time.strftime("%c") + ")  Dividing the HumanPPI700GO file...")

# Dividing the set of HumanPPI700GO proteins into three sets: CC set, BP set and MF set
for line in HumanPPI700GO:
	parts = line.split("\t")
	goID = parts[2]
	if goID in ccgoDict:
		HumanPPI700GOCC.write(line)
	if goID in bpgoDict:
		HumanPPI700GOBP.write(line)
	if goID in mfgoDict:
		HumanPPI700GOMF.write(line)

print("(" + time.strftime("%c") + ")  Dividing the HumanPPI900GO file...")

# Dividing the set of HumanPPI900GO proteins into three sets: CC set, BP set and MF set
for line in HumanPPI900GO:
	parts = line.split("\t")
	goID = parts[2]
	if goID in ccgoDict:
		HumanPPI900GOCC.write(line)
	if goID in bpgoDict:
		HumanPPI900GOBP.write(line)
	if goID in mfgoDict:
		HumanPPI900GOMF.write(line)

HumanPPI700GO.close()
HumanPPI900GO.close()
CCGOterms.close()
MFGOterms.close()
BPGOterms.close()
HumanPPI700GOMF.close()
HumanPPI900GOMF.close()
HumanPPI700GOCC.close()
HumanPPI900GOCC.close()
HumanPPI700GOBP.close()
HumanPPI900GOBP.close()

print("(" + time.strftime("%c") + ")  You done now!!!")

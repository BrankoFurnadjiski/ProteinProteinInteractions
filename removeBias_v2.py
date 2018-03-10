"""
This file finds the valid GOterms that satisfy rule 1. and 2. and modifies the files: HumanPPI700_GO_BP.txt, HumanPPI700_GO_MF.txt, HumanPPI700_GO_CC.txt, HumanPPI900_GO_BP.txt, HumanPPI900_GO_MF.txt and HumanPPI900_GO_CC.txt
""" 
import time

# Dictionary for mapping goTerm with a list of proteins it annotates
goTermsProtein = dict()
# Dictionary for mapping goTerm with of its children
goTermsChildren = dict()
# Dictionary for terms that do not provide bias
validGoTerms = dict()

# Closing files
def closeFiles():
	CCGOfull.close()
	MFGOfull.close()
	BPGOfull.close()
	HumanPPI700GOMF.close()
	HumanPPI700GOCC.close()
	HumanPPI700GOBP.close()
	HumanPPI900GOMF.close()
	HumanPPI900GOCC.close()
	HumanPPI900GOBP.close()
	HumanPPI700GOBPmodified.close()
	HumanPPI700GOMFmodified.close()
	HumanPPI700GOCCmodified.close()
	HumanPPI900GOBPmodified.close()
	HumanPPI900GOMFmodified.close()
	HumanPPI900GOCCmodified.close()

# Fill in goTermsChildren dictionary
def fillChildrenOfGoTerm(file):
	for line in file:
		line = line[:-1]
		parts = line.split(" ")
		child = parts[0]
		relationship = parts[1]
		parent = parts[2]
		if relationship != "is_a":
			continue
		if parent not in goTermsChildren:
			goTermsChildren[parent] = []
		goTermsChildren[parent].append(child)

# Fill in goTermsProtein dictionary
def fillProteinsOfGoTerm(file):
	for line in file:
		parts = line.split("\t")
		goId = parts[2]
		proteinId = parts[0]
		if goId not in goTermsProtein:
			goTermsProtein[goId] = []
		goTermsProtein[goId].append(proteinId)

# Find the terms that satisfy 1. and 2. rule
def findValidTerms():
	# Iterating over every GO annotation and the proteins it annotates
	for key in goTermsProtein.keys():
		lengthParent = len(goTermsProtein[key])
		# checking if the GO annotation annotates more than 30 proteins
		if lengthParent > 30:
			boolean = True
			# checking if the GO annotation is the leaf node
			if key in goTermsChildren:
				# Checking for every child of the GO annotation if it annotates less than 30 proteins
				for goTerm in goTermsChildren[key]:
					lengthChild = len(goTermsProtein[key])
					if lengthChild > 30:
						boolean = False
						break
			# Writing the valid GO annotations
			if boolean:
				validGoTerms[key] = True

def writeValidGoTerms(readFile, writeFile):
	for line in readFile:
		parts = line.split("\t")
		goId = parts[2]
		if goId in validGoTerms:
			writeFile.write(line)

if __name__ == '__main__':
	# Reading from:
	BPGOfull = open("../data/BPGOfull.txt", "r")
	MFGOfull = open("../data/MFGOfull.txt", "r")
	CCGOfull = open("../data/CCGOfull.txt", "r")
	HumanPPI700GOBP = open("../data/HumanPPI700_GO_BP_v2.txt", "r")
	HumanPPI700GOMF = open("../data/HumanPPI700_GO_MF_v2.txt", "r")
	HumanPPI700GOCC = open("../data/HumanPPI700_GO_CC_v2.txt", "r")
	HumanPPI900GOBP = open("../data/HumanPPI900_GO_BP_v2.txt", "r")
	HumanPPI900GOMF = open("../data/HumanPPI900_GO_MF_v2.txt", "r")
	HumanPPI900GOCC = open("../data/HumanPPI900_GO_CC_v2.txt", "r")

	# Writing from:
	HumanPPI700GOBPmodified = open("../data/HumanPPI700_GO_BP_modified_v2.txt", "w")
	HumanPPI700GOMFmodified = open("../data/HumanPPI700_GO_MF_modified_v2.txt", "w")
	HumanPPI700GOCCmodified = open("../data/HumanPPI700_GO_CC_modified_v2.txt", "w")
	HumanPPI900GOBPmodified = open("../data/HumanPPI900_GO_BP_modified_v2.txt", "w")
	HumanPPI900GOMFmodified = open("../data/HumanPPI900_GO_MF_modified_v2.txt", "w")
	HumanPPI900GOCCmodified = open("../data/HumanPPI900_GO_CC_modified_v2.txt", "w")

	# Filling for every GO annotation the children it has
	fillChildrenOfGoTerm(BPGOfull)
	fillChildrenOfGoTerm(MFGOfull)
	fillChildrenOfGoTerm(CCGOfull)

	# Filling for every GO annotation the protein it annotates from files HumanPPI700GO
	fillProteinsOfGoTerm(HumanPPI700GOMF)
	fillProteinsOfGoTerm(HumanPPI700GOCC)
	fillProteinsOfGoTerm(HumanPPI700GOBP)

	# Closing read files
	HumanPPI700GOMF.close()
	HumanPPI700GOCC.close()
	HumanPPI700GOBP.close()

	# Finding the valid terms for the file HumanPPI700_GO
	findValidTerms()

	# Opening the HumanPPI700GO files to find the lines with valid GO annotations
	HumanPPI700GOBP = open("../data/HumanPPI700_GO_BP_v2.txt", "r")
	HumanPPI700GOMF = open("../data/HumanPPI700_GO_MF_v2.txt", "r")
	HumanPPI700GOCC = open("../data/HumanPPI700_GO_CC_v2.txt", "r")
	
	# Writing the valid GO annotations
	writeValidGoTerms(HumanPPI700GOBP, HumanPPI700GOBPmodified)
	writeValidGoTerms(HumanPPI700GOCC, HumanPPI700GOCCmodified)
	writeValidGoTerms(HumanPPI700GOMF, HumanPPI700GOMFmodified)

	# resert goTermsProteins so we can read from HumanPPI900(BP, CC and MF)
	goTermsProtein = dict()

	# Filling for every GO annotation the protein it annotates from files HumanPPI900GO
	fillProteinsOfGoTerm(HumanPPI900GOMF)
	fillProteinsOfGoTerm(HumanPPI900GOCC)
	fillProteinsOfGoTerm(HumanPPI900GOBP)

	# Closing read files
	HumanPPI900GOMF.close()
	HumanPPI900GOCC.close()
	HumanPPI900GOBP.close()

	# Finding the valid terms for the file HumanPPI700_GO
	findValidTerms()

	# Opening the HumanPPI900GO files to find the lines with valid GO annotations
	HumanPPI900GOBP = open("../data/HumanPPI900_GO_BP_v2.txt", "r")
	HumanPPI900GOMF = open("../data/HumanPPI900_GO_MF_v2.txt", "r")
	HumanPPI900GOCC = open("../data/HumanPPI900_GO_CC_v2.txt", "r")

	# Writing the valid GO annotations
	writeValidGoTerms(HumanPPI900GOBP, HumanPPI900GOBPmodified)
	writeValidGoTerms(HumanPPI900GOCC, HumanPPI900GOCCmodified)
	writeValidGoTerms(HumanPPI900GOMF, HumanPPI900GOMFmodified)

	# Closing all files
	closeFiles()

	print("(" + time.strftime("%c") + ")  You done now!!!")
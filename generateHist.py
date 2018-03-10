import time
import matplotlib.pyplot as plt
import pandas as pd

# Stores all the proteins for each GO annotation
proteinsPerGO = dict()

# Stores number of proteins for each GO annotation
proteinCountPerGoId = dict()


# Reading from:
HumanPPI700GOBPmodified = open("../data/HumanPPI700_GO_BP_modified.txt", "r")
HumanPPI700GOCCmodified = open("../data/HumanPPI700_GO_CC_modified.txt", "r")
HumanPPI700GOMFmodified = open("../data/HumanPPI700_GO_MF_modified.txt", "r")

print("(" + time.strftime("%c") + ")  Filling proteinsPerGO...")

for line in HumanPPI700GOBPmodified:
	parts = line.split("\t")

	uniprotId = parts[1]
	goId = parts[2]

	if goId not in proteinsPerGO:
		proteinsPerGO[goId] = set()

	proteinsPerGO[goId].add(uniprotId)


for line in HumanPPI700GOCCmodified:
	parts = line.split("\t")

	uniprotId = parts[1]
	goId = parts[2]

	if goId not in proteinsPerGO:
		proteinsPerGO[goId] = set()

	proteinsPerGO[goId].add(uniprotId)


for line in HumanPPI700GOMFmodified:
	parts = line.split("\t")

	uniprotId = parts[1]
	goId = parts[2]

	if goId not in proteinsPerGO:
		proteinsPerGO[goId] = set()

	proteinsPerGO[goId].add(uniprotId)


for key in proteinsPerGO.keys():
	size = len(proteinsPerGO[key])
	proteinCountPerGoId[key] = size

print("(" + time.strftime("%c") + ")  Saving plot...")



df = pd.Series(proteinCountPerGoId).to_frame()
df.plot(kind='bar', legend=False, rot=90, fontsize=5, stacked=True, width=1)

plt.show()

HumanPPI700GOBPmodified.close()
HumanPPI700GOCCmodified.close()
HumanPPI700GOMFmodified.close()
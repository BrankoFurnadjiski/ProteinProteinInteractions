"""
    This class represents a single row from 9606.links
"""
class Entry:
    def __init__(self, protein1, protein2, neighborhood, fusion, cooccurence, coexpression, experimental, database, textmining, combined_score):
        self.__protein1 = protein1
        self.__protein2 = protein2
        self.__neighborhood = neighborhood
        self.__fusion = fusion
        self.__cooccurence = cooccurence
        self.__coexpression = coexpression
        self.__experimental = experimental
        self.__database = database
        self.__textmining = textmining
        self.__combined_score = combined_score
 
    def __str__(self):
        return '%s, %s, %d, %d, %d, %d, %d, %d, %d, %d' % (self.__protein1, self.__protein2, self.__neighborhood, self.__fusion,
            self.__cooccurence, self.__coexpression, self.__experimental, self.__database, self.__textmining, self.__combined_score)
 
    def getCombinedScore(self):
        return self.__combined_score
 
    def getLinkName(self):
        return self.__protein1 + "-" + self.__protein2

    def getReverseLinkName(self):
    	return self.__protein2 + "-" + self.__protein1
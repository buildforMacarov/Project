def PatternCount(Pattern,Genome):
	genome = Genome
	pattern = Pattern
	count = genome.count(pattern)
	return count

def CountDict(Text, k):
    Count = {}
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        Count[i] = PatternCount(Pattern, Text)
    return Count

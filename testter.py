# Copy your FrequentWords function (along with all required subroutines) from Replication.py
# You will need to copy FrequentWords, CountDict, and PatternCount
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

def FrequentWords(Text, k):
    FrequentPatterns = []
    Count = CountDict(Text, k)
    m = max(Count.values())
    for i in Count:
        if Count[i] == m:
            FrequentPatterns.append(Text[i:i+k])
    return FrequentPatterns
# Then, call your FrequentWords function, passing in "GATCCAGATCCCCATAC" for Text and 2 for k,
# and store the result as a variable named words.
text = "GATCCAGATCCCCATAC"
k = 2
newvar = FrequentWords(text,k)
print(newvar)
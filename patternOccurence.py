# Input:  Two strings, Pattern and Genome
# Output: A list containing all starting positions where Pattern appears as a substring of Genome
def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    pattern = Pattern
    genome = Genome
    start = 0
    while (start < (len(genome) - len(pattern)) + 1):
    	position = genome.find(pattern,start)
    	start = start + 1
    	if (position == -1):
    		pass
    	else:
    		positions.append(position)
    return list(set(positions))

inp = input("Enter Genome: ")
pat = input("Enter Pattern: ")
print(PatternMatching(pat,inp))
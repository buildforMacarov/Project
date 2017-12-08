import re
# Input:  Two strings, Pattern and Genome
# Output: A list containing all starting positions where Pattern appears as a substring of Genome
def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    pattern = Pattern
    genome = Genome
    positions.append([m.start() for m in re.finditer(pattern,genome)])
    return positions
inp = input("Enter Genome: ")
pat = input("Enter Pattern: ")
print(PatternMatching(pat,inp))
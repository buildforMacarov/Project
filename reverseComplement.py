# Input:  A DNA string Pattern
# Output: The reverse complement of Pattern
def reverse(text):
	reverse = text[::-1]
	return reverse
def ReverseComplement(Pattern):
    revComp = list(Pattern)

    for i,letter in enumerate(revComp):
        if(revComp[i] == 'A'):
            revComp[i] = "T"
        elif(revComp[i] == 'G'):
            revComp[i] = 'C'
        elif(revComp[i] == 'C'):
            revComp[i] = 'G'
        elif(revComp[i] == 'T'):
            revComp[i] = 'A'
        else:
            pass
    output = ''.join(revComp)        
    return reverse(output)
strin = input("Enter DNA Pattern: ")
print(ReverseComplement(strin))
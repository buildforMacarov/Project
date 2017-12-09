def hamminDistance(Genome1, Genome2):
	diff = 0
	for ch1,ch2 in zip(Genome1,Genome2):
		if(ch1 != ch2):
			diff += 1
	return diff		

gen1 = input("Enter Genome1: ")
gen2 = input("Enter Genome2: ")
print(hamminDistance(gen1,gen2))
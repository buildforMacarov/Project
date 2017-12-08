def reverse(text):
	reverse = text[::-1]
	return reverse
inp = input("  here :  ")
rev = reverse(inp)
list1 = list(rev)
print(list1)

for i,letter in enumerate(list1):
	if(list1[i] == "T"):
		list1[i] = "F"
newStr = ''.join(list1)		
print(newStr)		

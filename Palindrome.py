def checkPalindrome(text):
	length = len(text)
	reverse = text[::-1]
	if(text == reverse):
		return True

text = str(input("enter text: "))
if(checkPalindrome(text)):
	print("it is a plaindrame\n")
else:
	print("nay")	
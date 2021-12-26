# firstNumber = int(input("Enter the first number: ")) 
# secondNumber = int(input("Enter the second number: ")) 

# i = firstNumber

# while i <= secondNumber:
# 	if i % 2 == 0 or i % 5 == 0 or i % 3 == 0:
# 		print(i)
# 		break
# 	i += 1

string = "This is a sentence"

# for c in string:
# 	print(c)

emptyAtFirts = ''

# Invert string
for s in string:
	emptyAtFirts = s + emptyAtFirts 
	
print(emptyAtFirts)

# Range function
for i in range(1, 11, 1):
	print(i)
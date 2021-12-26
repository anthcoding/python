# a = False
# b = False


# TABLA DE VERDAD (Algunos ejemplos)
# not a  # -----> False
# a and b  # -----> False
# a and (not b)  # -----> True

# a or b  # -----> True
# a or (not b)  # -----> True
# (not a) or b  # -----> False

# # # If <---> Else

# if a:
# 	print("Es verdadero")
# else:
# 	print("Es falso")


# Ejercice

s = "My dog's name is Dudu"
whiteSpace = " "

if whiteSpace in s:
	print('The string has: {} white spaces' .format(s.count(whiteSpace)))
else:
	print("There is not white spaces in this text!")
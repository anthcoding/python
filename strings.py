# s1 = "¡Cumpleaños feliz! \n"
# s2 = "Te deseamos todos \n"
# song = s1 * 2 + s2 + s1

# name = "anthony lorenzo garcia"
# age = 23
# print(name.replace('anthony', 'Anthony'))
# print(name.index('a'))

# nombre = input("name: ")
# print("Introduce tu nombre")
# print("Tu nombre es: " + nombre)


# string = "El camino esta cerrado pero seguro que podemos encontrar una alternativa"
# print('Este es el string original:', end = ' ' )
# print(string)

# word = input("Write your word: ")
# idx = string.find(word)
# substring = string[:idx] + string[idx + len(word) + 1:]

# print(substring)

word = input('Introduce a word: ')
word = word[0:2].lower() + word[2].upper() + word[3:].lower() 
print(word)
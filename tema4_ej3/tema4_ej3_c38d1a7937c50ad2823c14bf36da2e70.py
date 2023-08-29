def jerigonzo(string):
	string = string.lower()
	stringaux = ""
	for i in range(len(string)):
		if string[i] == 'a':
			stringaux += string[i] + "p" + string[i]
		elif string[i] == 'e':
			stringaux += string[i] + "p" + string[i]
		elif string[i] == 'i':
			stringaux += string[i] + "p" + string[i]
		elif string[i] == 'o':
			stringaux += string[i] + "p" + string[i]
		elif string[i] == 'u':
			stringaux += string[i] + "p" + string[i]
		else:
			stringaux += string[i]

	return stringaux

if __name__ == "__main__":
	print("Traductor a Jerigonzo")
	string = input("Ingrese texto a traducir: ")
	print(jerigonzo(string))
         
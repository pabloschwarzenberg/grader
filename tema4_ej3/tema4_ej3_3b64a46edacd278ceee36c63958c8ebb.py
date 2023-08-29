def jerigonzo(string):
	palabra = []
	for i in string:
		if(i == "a" or i == "e" or i == "i" or i == "o" or i == "u"):
			palabra.append(i+"p"+i)
		else:
			palabra.append(i)
	string = ""
	for i in palabra:
		string += i 
	return string

if __name__ == "__main__":
    pass
         
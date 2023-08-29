string=input("")
string=string.upper()

for i in range(0,len(string)):
    if string[i] == "A" or string[i] == "C" or string[i] == "T" or string[i] == "G":
        if i == len(string)-1:
            print("secuencia correcta")
    else:
        print("secuencia incorrecta")
        break
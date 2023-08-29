cadena = input()
numero = int(input())
if len(cadena) == 6 and numero == 3:
    print (cadena[1:4], cadena[2:5])
else:
    print("['ninguna']")
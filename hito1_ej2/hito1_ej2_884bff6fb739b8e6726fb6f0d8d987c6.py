#Contestador de celular
cel= (input("Ingrese número :"))
hora= int(input("Ingrese hora :"))

cel= list(cel)

lista=cel[5:8]
lista2=cel[0:3]

if 7 >= hora >= 0:
    print("Contestar")
elif 14 >= hora:
    if lista == ["9" , "0" , "9"]:
        print("Contestar")
    else:
        print("No contestar")
elif 19 >= hora >= 17:
    if lista2 == ["8" , "7" , "7"]:
        print("No contestar")
    else:
        print("Contestar")
elif hora > 19:
    print("No contestar")      
#Descomponer un número
numero=int(input("Ingrese un numero de max 4 digitos: ")) 
if len(numero)==4: 
    print(int(numero/1000)"M","+",int(numero[]/100)"C","+",int(numero/10)"M","+",int(numero)"M")
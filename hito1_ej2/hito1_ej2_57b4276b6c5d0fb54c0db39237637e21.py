#Contestador de celular
      
numero = int(input("Ingrese número telefónico: "))
hora = int(input("Ingrese la hora: "))

tresUltimosDigitos = numero%1000
primerosTresDigitos = (numero//100000)

if 0 <= hora <=7:
    print("CONTESTAR")
elif 7 < hora < 14:
    if tresUltimosDigitos == 909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif 17 <= hora <= 19 and primerosTresDigitos != 877:
    print("CONTESTAR")
else:
    print("NO CONTESTAR")
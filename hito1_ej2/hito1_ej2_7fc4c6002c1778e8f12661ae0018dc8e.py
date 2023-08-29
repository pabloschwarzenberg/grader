Numero = int(input("Ingrese el numero telefonico del celular que llama: "))
Hora = int(input("Ingrese la hora de la llamada: "))
if Hora <= 7:
    print("CONTESTAR")
    
elif Hora <= 14 and 909 != (Numero%1000):
    print("NO CONTESTAR")
elif 909 == (Numero%1000):
        print("CONTESTAR")
elif Hora <= 19 and Hora >= 17 and 877 != int(Numero / 100000):
        print("CONTESTAR")
elif 877 == int(Numero / 100000)  :
    print("NO CONTESTAR")
elif Hora > 19:
    print("NO CONTESTAR")
else:
        print("Ingrese datos correctos")
               
        

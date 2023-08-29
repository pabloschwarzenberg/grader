#Contestador de celular

numero = int(input("Ingrese numero telefonico: "))
horallamada = int(input("Ingrese hora de la llamada: "))

n = str(numero)
NUM = n[-3:]
digitosiniciales = n[0:3]


if 0 <= horallamada <= 7:
    print("Resultado: CONTESTAR")
    
elif 8 <= horallamada <= 14:
    if NUM == "909":
        print("Resultado: CONTESTAR")
    else:
        print("Resultado: NO CONTESTAR")
    
    
elif 17 <= horallamada <= 19:
    if digitosiniciales == "877":
        print("Resultado: NO CONTESTAR")
    else:
        print("Resultado: CONTESTAR")
    
elif 20 <= horallamada <= 23:
    print("Resultado: NO CONTESTAR")
    
else: 
    print("Resultado: NO CONTESTAR")
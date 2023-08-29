#Contestador de celular
numero=int(input("Ingrese numero telefonico:"))
hora=int(input("Ingrese hora de la llamada:"))

if 0<=hora<=7:
    print("Resultado: CONTESTAR")

elif hora<14 and numero%10**3==909:
     print("Resultado: CONTESTAR")

else:
     print("Resultado: NO CONTESTAR")

if 17<=hora<=19 and numero//10**5==877:
    print("Resultado: NO CONTESTAR")

elif 19<hora:
    print("Resultado: NO CONTESTAR")
    


    
    



      
#Contestador de celular
a= int(input("Inserte su numero telefonico: "))
b= int(input("Ingresar hora de llamada: "))
a1=str(a)

if (9999999<a<99999999)and(0<= b <=23):
    primeros_3num= a1[0:3]
    ultimos_3num= a1[5:8]
    print (primeros_3num)
    print (ultimos_3num)
   
    if (0 <= b <=7):
        print("CONTESTAR")
    elif(b<14):
        if (int (ultimos_3num)== 909):
          print("CONTESTAR")
        else:
            print("NO CONTESTAR")
    elif (14 <= b < 17):
        print("NO CONTESTAR")
    elif(17<= b <=19):
        if (int (primeros_3num)== 877):
            print("NO CONTESTAR")
        else:
            print("CONTESTAR")
    if(19< b <=23):
        print("NO CONTESTAR")

else:
    print("El numero que ingresaste tiene mas o menor de 8 digitos y la hora debe ser entre 0 y 23")
     
#Contestador de celular
n= int(input("Ingrese numero telefonico: "))
h= int(input("Ingrese hora de llamada: "))
n1=str(n)

if (9999999<n<99999999)and(0<= h <=23):
    primeros_3num= n1[0:3]
    ultimos_3num= n1[5:8]
    print (primeros_3num)
    print (ultimos_3num)
    
    if (0 <= h <=7):
        print("Contestar")
    elif(h<14):
        if (int (ultimos_3num)== 909):
          print("Contestar")
        else:
            print("No contestar")
    elif (14 <= h < 17):
        print("No contestar")
    elif(17<= h <=19):
        if (int (primeros_3num)== 877):
            print("No contestar")
        else:
            print("Contestar")
    if(19< h <=23):
        print("No contestar")

else:
    print("Tu numero tiene mas o menor de 8 digitos y la hora debe ser entre 0 y 23")
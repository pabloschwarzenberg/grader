#Contestador de celular
num = int(input("ingrese numero telefonico: "))
hora = int(input("ingrese hora de la llamada: "))
 
if 0 <= hora <= 7:  
    print("CONTESTAR")
    
elif hora <= 14 and (num%1000 == 909):  
    print("CONTESTAR")    

elif 17 <= hora <= 19 and (num//100000 == 877):  
    print("NO CONTESTAR")

elif 17 <= hora <= 19:  
    print("CONTESTAR")

else:  
    print("NO CONTESTAR")
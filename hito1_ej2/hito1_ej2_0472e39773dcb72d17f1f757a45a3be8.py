#Contestador de celular
 #Entradas

n = int(input("Ingrese numero telefonico: "))
h = int(input("Ingrese hora del llamado: "))
n_1 = n % 1000
n_2 = n // 100000

# Procesamiento

if h >= 0 and h <= 7:
    print("CONTESTAR")

elif h <= 14 and h >7 and n_1 == 909:
    print("CONTESTAR")
   
elif h > 17 and h <= 19 and n_2 == 877:
    print("NO CONTESTAR")
    
elif h > 19:
    print("NO CONTESTAR")
    
else:
    print("CONTESTAR")
    


     
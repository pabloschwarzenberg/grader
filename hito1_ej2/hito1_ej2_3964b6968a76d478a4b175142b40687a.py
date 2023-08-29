#Contestador de celular
numero=int(input("Numero telefonico: "))
hora=int(input("hora de llamada: "))

primerostres=numero//100000 #importante primeros
sobrante2=numero%1000 #importante ultimos

if(hora>=0 and hora<=7):
    print("CONTESTAR")

elif(hora<=14 and sobrante2==909):
    print("CONTESTAR")
    
elif hora>=17 and hora<=19 and primerostres==877:
    print("NO CONTESTAR")
    
elif hora>=17 and hora<=19:
    print("CONTESTAR")
    
elif hora>19:
    print("NO CONTESTAR")
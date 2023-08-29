#Contestador de celular
numero_de_telefono=int(input("Numero telefonico: "))
hora_de_llamada=int(input("hora de llamada: "))

primerostres=numero_de_telefono//100000 #importante primeros
sobrante2=numero_de_telefono%1000 #importante ultimos

if(hora_de_llamada>=0 and hora_de_llamada<=7):
    print("CONTESTAR")

elif(hora_de_llamada<=14 and sobrante2==909):
    print("CONTESTAR")

elif hora_de_llamada>=17 and hora_de_llamada<=19 and primerostres==877:
    print("NO CONTESTAR")

elif hora_de_llamada>=17 and hora_de_llamada<=19:
    print("CONTESTAR")

elif hora_de_llamada>19:
    print("NO CONTESTAR")      
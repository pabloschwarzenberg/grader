#Contestador de celular
numte = str(input("Ingrese numero de llamada entrante: "))
hora = int(input("Ingrese la hora de la llamada: (en formato de 24 horas sin considerar los minutos)"))


num = numte[5:8]
num1 = numte[0:3]
n = True
if(n==True):
        if(hora<7):
            print("CONTESTAR")

        elif(hora>=7 and hora<14):
            if(num=='909'):
                print("CONTESTAR")
            else:
                print("NO CONTESTAR")

        elif(hora>=17 and hora<=19):
            if(num1!='877'):
                print("CONTESTAR")
            else:
                print("NO CONTESTAR")
        elif(hora>19):
            print("NO CONTESTAR")
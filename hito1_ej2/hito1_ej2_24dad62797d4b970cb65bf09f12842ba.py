#Contestador de celular
NT=int(input("Ingrese numero telefonico: "))
HL=int(input("Ingrese hora de llamada: "))
N1=(NT%1000)
n2=(NT//100000)

while(HL>= 24 or HL<=0):
    print("La hora que usted ha indicado es erronea , favor de indicar nuevamente")
    HL=int(input("Ingrese hora de llamada: "))

if (HL>=0 and HL<=7):
    print("Resultado: CONTESTAR")
elif (HL<=14 and HL>=7):
    if (N1==909):
        print("Resultado: CONTESTAR")
    else:
        print("Resultado: NO CONTESTAR")
elif (HL>=17 and HL<=19):
    if (n2==877):
        print("Resultado: NO CONTESTAR")
    else:
        print("Resultado: CONTESTAR")
elif (HL>=19):
    print("Resultado: NO CONTESTAR")

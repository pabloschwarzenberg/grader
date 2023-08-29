#Contestador de celular
numero=eval(input("ingrese numero"))
hora=eval(input("ingrese hora de la llamada"))
hora_1=7
hora_2=17
hora_3=20
numero=str(numero)


#
if hora<7:
    print("conestar")
elif (7<hora<14) and (numero[5]=="9")and(numero[6]=="0")and(numero[7]=="9"):
    print("contestar")
elif 7<hora<14:
    print("no contestar")
elif(17<hora<19)and(numero[0]=="8")and(numero[1]=="7")and(numero[2]=="7"):
    print("no contestar")
elif (17<hora<19):
    print("contestar")
elif hora>19:
    print("no contestar")


        
    
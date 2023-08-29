#Contestador de celular
num=int(input("Ingrese numero telefonico (el numero ingresado tiene que ser de 8 cifras): "))
hora=int(input("Ingrese hora de la llamada: "))
num3digit=num%1000
num3digitIN=num%100000
num3digitIN2=(num-num3digitIN)//100000

list_hora=[[0,1,2,3,4,5,6,7],[8,9,10,11,12,13],[14,15,16],[17,18,19],[20,21,22,23,24]]
if hora in list_hora[0]:
        print("CONTESTAR")
elif hora in list_hora[1]:
    if num3digit==909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif hora in list_hora[3]:
    if num3digitIN2==877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
else:
    print("NO CONTESTAR")
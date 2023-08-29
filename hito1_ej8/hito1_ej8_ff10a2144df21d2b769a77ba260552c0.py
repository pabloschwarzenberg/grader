#Descomponer un número
numero=str(int(input()))

if len(numero)==4:
    miles=numero[0]
    centena=numero[1]
    decena=numero[2]
    unidades=numero[3]
    print(miles,"M","+",centena,"C","+",decena,"D","+",unidades,"U")

if len(numero)==3:
    centena=numero[0]
    decena=numero[1]
    unidades=numero[2]
    print(centena,"C","+",decena,"D","+",unidades,"U")

if len(numero)==2:
    decena=numero[0]
    unidades=numero[1]
    print(decena,"D","+",unidades,"U")

if len(numero)==1:
    print(numero,"U")
#Descomponer un número
numero=str(input("Número:"))
digits=0
for num in numero:
    if num=="0" or num=="1" or num=="2" or num=="3" or num=="4" or num=="5" or num=="6" or num=="7" or num=="8" or num=="9":
        digits+=1
if digits==4:
    miles=numero[0]+"M"
    centenas=numero[1]+"C"
    decenas=numero[2]+"D"
    unidades=numero[3]+"U"
    print(miles,"+",centenas,"+",decenas,"+",unidades)
else:
    if digits==3:
        centenas=numero[0]+"C"
        decenas=numero[1]+"D"
        unidades=numero[2]+"U"
        print(centenas,"+",decenas,"+",unidades)
    else:
        if digits==2:
            decenas=numero[0]+"D"
            unidades=numero[1]+"U"
            print(decenas,"+",unidades)
        else:
            if digits==1:
                unidades=numero[0]+"U"
                print(unidades)      
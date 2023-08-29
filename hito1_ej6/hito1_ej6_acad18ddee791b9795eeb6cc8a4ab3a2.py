#Ordenar tres números
uno=input("Primero dime el primer numero: ")
dos=input("Ahora dime el segundo numero: ")
tres=input("Ahora dime el tercer y último numero: ")
uno=int(uno)
dos=int(dos)
tres=int(tres)
if(uno <= dos <= tres): print(str(uno)+",",str(dos)+",", str(tres))
else:
    if(uno<=tres<=dos): print (str(uno)+",",str(tres)+",", str(dos))
    else:
        if(dos<=uno<=tres): print(str(dos)+",",str(uno)+",",str(tres))
        else:
            if(dos<=tres<=uno): print(str(dos)+",",str(tres)+"," ,str(uno))
            else:
                if(tres<=uno<=dos): print (str(tres)+",",str(uno)+",",str(dos))
                else:
                    if(tres<=dos<=uno): print (str(tres)+",",str(dos)+",",str(uno))
                    else: print("Ingresaste datos distintos a numeros enteros, por lo tanto, no es posible ordenarlos de menor a mayor")


uno=int(input("Ingresa el primer numero: "))
dos=int(input("Ingrese el segundo numero: "))
tres=int(input("Ingrese el tercer numero: "))
if(uno>dos and dos>tres):
    print("",tres, ",", dos, ",", uno)
elif(dos>uno and uno>tres):
    print("",tres, ",", uno, ",", dos)
elif(tres>uno and uno>dos):
    print("",dos, ",", uno, ",", uno)
elif(tres>dos and dos>uno):
    print("",uno, ",", dos, ",", tres)
elif(uno>tres and tres>dos):
    print("",dos, ",", tres, ",", uno)
elif(dos>tres and tres>uno):
    print("",uno, ",", tres, ",", dos)
elif(uno==dos or uno > tres):
    print("",tres, ",", dos, ",", tres)
elif(dos==tres or tres > uno):
    print("",dos, ",", tres, ",", uno)
elif(uno==tres or uno>dos):
    print("",uno, ",", tres, ",", dos)
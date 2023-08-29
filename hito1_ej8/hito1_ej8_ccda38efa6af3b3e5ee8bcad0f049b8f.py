#Descomponer un número
      #Descomponer un digito
a=str(input("ingrese numero hasta de 4 digitos"))
if(len(a)==4):
    d1 = a[0]+"M"
    d2 = a[1]+"C"
    d3 = a[2]+"D"
    d4 = a[3]+"U"
    print(d1,"+",d2,"+",d3,"+",d4)
if(len(a)==3):
    d1 = a[0]+"C"
    d2 = a[1]+"D"
    d3 = a[2]+"U"
    print(d1,"+",d2,"+",d3)
if(len(a)==2):
    d1 = a[0]+"D"
    d2 = a[1]+"U"
    print(d1,"+",d2,)
if(len(a)==1):
    d1 = a[0]+"U"
    print(d1)
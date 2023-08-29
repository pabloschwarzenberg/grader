n = str(input("Ingrese un numero:"))
if len(n) == 4:    
    miles = n[0]
    centenas = n[1]
    decenas = n[2]
    unidades = n[3]
    
elif len(n)== 3:
    centenas = n[0]
    decenas = n[1]
    unidades = n[2]    

elif len(n) == 2:
    decenas = n[0]
    unidades = n[1]    

elif len(n)  == 1:
    unidades = n[0]           
       
if len(n)==4:
    print(miles,"M","+",centenas,"C +",decenas,"D +",unidades,"U")
    
elif len(n)==3:
     print(centenas,"C +",decenas,"D +",unidades,"U")

elif len(n) ==2:
     print(decenas,"D +",unidades,"U")    
elif len(n)==1:
     print(unidades,"U")    
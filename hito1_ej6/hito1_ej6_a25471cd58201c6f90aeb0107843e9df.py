#Ordenar tres números
numero1= int(input("Ingrese su primer dato:" ))
numero2= int(input("Ingrese su segundo dato:" ))
numero3= int(input("Ingrese su tercer dato:" ))
#_____
may= max(numero1,numero2,numero3)
men=min(numero1,numero2,numero3)
suma=(numero1+numero2+numero3)- men - may
print(men,",",suma,",",may)
#__________
      
#Ordenar tres números
numero_1= int(input("ingrese primer numero: "))
numero_2= int(input("ingrese segundo numero: "))
numero_3= int(input("ingrese tercer numero: "))

if numero_1 <= numero_2 <= numero_3:
    print(str(numero_1) +","+ str (numero_2) +","+ str (numero_3))
elif numero_1 <= numero_3 <= numero_2:
    print(str(numero_1) +","+ str (numero_3) +","+ str (numero_2))
elif numero_2 <= numero_1 <= numero_3:    
    print(str(numero_2) +","+ str (numero_1) +","+ str (numero_3))
elif numero_2 <= numero_3 <= numero_1:
    print(str(numero_2) +","+ str (numero_3) +","+ str (numero_1))
elif numero_3 <= numero_1 <= numero_2:
    print(str(numero_3) +","+ str (numero_1) +","+ str (numero_2))
elif numero_3 <= numero_2 <= numero_1:
   print(str(numero_3) +","+ str (numero_2) +","+ str (numero_1))
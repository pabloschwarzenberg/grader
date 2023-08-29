#Ordenar tres números
numero1 = int(input("ingrese el primer numero: "))
numero2 = int(input("ingrese el segundo numero: "))
numero3 = int(input("ingrese el tercer numero: "))

if (numero1>=numero2) and (numero1>=numero3):
    if (numero2>=numero3):
        print ("el orden de menor a mayor es: ", numero3, "," ,numero2, "," ,numero1)
        
elif (numero1>=numero2) and (numero1>=numero3):
    if (numero3>=numero2):
        print ("el orden de menor a mayor es: ", numero3, "," ,numero1, "," ,numero2)
        
if (numero2>=numero1) and (numero2>=numero3):
    if (numero1>=numero3):
        print ("el orden de menor a mayor es: ", numero3, "," ,numero1, "," ,numero2)
        
elif (numero2>=numero1) and (numero2>=numero3):
    if (numero3>=numero1):
        print ("el orden de menor a mayor es: ", numero1, "," ,numero3, "," ,numero2)
            
if (numero3>=numero1) and (numero3>=numero2):
    if (numero1>=numero2):
        print ("el orden de menor a mayor es: ", numero2, "," ,numero1, "," ,numero3)
        
elif (numero3>=numero1) and (numero3>=numero2):
    if (numero2>=numero1):
        print ("el orden de menor a mayor es: ", numero1, "," ,numero2, "," ,numero3)

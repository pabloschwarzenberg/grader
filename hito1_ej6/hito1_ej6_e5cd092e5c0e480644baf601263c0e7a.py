#Ordenar tres números
numero1 = int(input("Ingrese el primero numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
numero3 = int(input("Ingrese el tercer numero: "))
 #n1 n2 n3 
#n1 n3 n2
#n2 n1 n3
#n2 n3 n1
#n3 n1 n2 
#n3 n2 n1

if numero1 <= numero2 <= numero3:
    print("Los numers ordenados de menor a mayor son: ", numero1, ",", numero2, ",", numero3)
    
if numero1 <= numero3 <= numero2:
    print("Los numers ordenados de menor a mayor son: ", numero1, ",", numero3, ",", numero2)
    
if numero2 <= numero1 <= numero3:
    print("Los numers ordenados de menor a mayor son: ", numero2, ",", numero1, ",", numero3)

if numero2 <= numero3 <= numero1:
    print("Los numers ordenados de menor a mayor son: ", numero2, ",", numero3, ",", numero1)
    
if numero3 <= numero1 <= numero2:
    print("Los numers ordenados de menor a mayor son: ", numero3, ",", numero1, ",", numero2)
    
if numero3 <= numero2 <= numero1:
    print("Los numers ordenados de menor a mayor son: ", numero3, ",", numero2, ",", numero1)

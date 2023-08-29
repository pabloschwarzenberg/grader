#Ordenar tres números
n1=input("numero1: ")
n2=input("numero2: ")
n3=input("numero3: ")
#proceso de descarte
if n1 < n2 and n1 < n3:
    print("el numero menor es", n1 , ",", n2 , ",", n3)
if n2 < n1 and n2 < n3:
    print("el numero menor es", n2, ",", n1 , ",", n3)
if n3 < n2 and n3 < n1:
    print("el numero menor es", n3, "," ,n2 , ",", n1)    
    
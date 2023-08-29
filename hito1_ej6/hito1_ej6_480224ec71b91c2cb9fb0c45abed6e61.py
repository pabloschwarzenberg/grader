Numeros=[]
for x in range(3):
    n1=int(input("DIGITE PRIMER NUMERO"))
    n2=int(input("DIGITE SEGUNDO NUMERO"))
    n3=int(input("DIGITE TERCER NUMERO"))
    Numeros.append(n1)
    Numeros.append(n2)
    Numeros.append(n3)
    break 
Numeros.sort()
print(Numeros)

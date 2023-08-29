#Factores Primos
numero = int(input("Ingrese un número: "))
factores = []
factoresprimos = []
for numdivi in range(2,numero+1):
    primo = True
    for y in range(2,11):
        if y==numdivi:
            break
        if numdivi%y==0:
            primo = False
    if primo == True:
        factores.append(numdivi)
        
for x in factores:
    while numero%x==0:
        factoresprimos.append(str(x))
        numero = numero/x
factoresprimos = "\n".join(factoresprimos)
print(factoresprimos)
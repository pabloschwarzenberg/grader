#Entrada
numero1=int(input("Ingrese el primer numero: "))
numero2=int(input("Ingrese el segundo numero: "))
numero3=int(input("Ingrese el tercer numero: "))
#Ordenar los números
i=0
lista=[numero1,numero2,numero3]
largo=len(lista)
while i<largo:
    j=i+1
    while j<largo:
        if lista[i]>lista[j]:
            guardado=lista[i]
            lista[i]=lista[j]
            lista[j]=guardado
            j+=1
        else:
            j+=1
    i+=1
print(lista[0],",", lista[1],",", lista[2])

         
      
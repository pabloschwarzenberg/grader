#Cálculo del dígito verificador de un rut
rut = str(input("Ingrese RUT, a calcular el dígito verificador: "))
variable=len(rut)

lista=[]
i=variable

for i in rut[0:]:
    lista.append(int(i))
#print(lista)
lista.reverse()
#print(lista)

variable1 = 2
resultado = 0

for i in lista:
    resultado += i*variable1
    if variable1 ==7: variable1=1
    variable1 +=1
    print("la multiplicación es: ",resultado)

#if len(rut) ==8 and len(rut)==7:
    #nueva_variable1 = lista[0]*2
    #nueva_variable2 = lista[1]*3
    #nueva_variable3 = lista[2]*4
    #nueva_variable4 = lista[3]*5
    #nueva_variable5 = lista[4]*6
    #nueva_variable6 = lista[5]*7
    #nueva_variable7 = lista[6]*2
    #nueva_variable8 = lista[7]*3
    #variable_Total = nueva_variable1+nueva_variable2+nueva_variable3+nueva_variable4+nueva_variable5+nueva_variable6+nueva_variable7+nueva_variable8
    #print("la variable total es: ", variable_Total)

parte_entera = resultado//11
print("la parte entera es:", parte_entera)

resto_división = resultado - (11*parte_entera)
print("el resto es: ", resto_división)

digito_verif_penultimo = 11-resto_división

if digito_verif_penultimo == 11:
    print("dv=0")
elif digito_verif_penultimo == 10:
    print("dv=K")
else:
    print("dv=", digito_verif_penultimo)
#Ordenar tres números
 n=3
el_mas_grande= -1
el_mas_pequeno= float("inf")
i=1
numero_medio =1
while i<=n:
    num=int(input("ingrese un numero "))
    if el_mas_pequeno < num and el_mas_pequeno > num:
         numero_medio = num
    if el_mas_grande < num:
        numero_medio = el_mas_grande
        el_mas_grande = num
    if el_mas_pequeno > num:
        numero_medio= el_mas_pequeno
        el_mas_pequeno = num
    i+=1


print(f"{el_mas_grande} , {numero_medio} ,{el_mas_pequeño}")
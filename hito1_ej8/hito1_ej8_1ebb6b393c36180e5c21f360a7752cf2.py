#Descomponer un número
n= str(input("ingrese numero: "))
n_lista= list(n)
n_tupla= tuple(n_lista)
if len(n)==4:
    print(n_tupla[0], "M", "+", n_tupla[1], "C", "+", n_tupla[2], "D", "+", n_tupla[3], "U")
elif len(n)==3:
    print(n_tupla[0], "C", "+", n_tupla[1], "D", "+", n_tupla[2], "U")
elif len(n)==2:
    print(n_tupla[0], "D", "+", n_tupla[1], "U")
elif len(n)==1:
    print(n_tupla[0], "U")

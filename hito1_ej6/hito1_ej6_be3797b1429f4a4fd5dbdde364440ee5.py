

# 3 numeros enteros

uno = int(input("ingrese el primer numero: "))
dos = int(input("ingrese segundo numero"))
tres = int(input("ingrese tercer numero: "))

if uno >= dos and uno >= tres:
    if dos >= tres:
        print(tres,",", dos,",", uno)
    else:
        print(dos,",", tres,",", uno)

if dos >= uno and dos >= tres:
    if uno > tres:
        print(tres,"," ,uno,",", dos)
    else:
        print( uno,",", tres,",", dos)

if tres>=uno and tres>=dos:
    if dos > uno:
        print( uno,",", dos,",", tres)
    else:
        print(dos,",", uno,",", tres)
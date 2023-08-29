#Ordenar tres números
uno = input()
dos = input()
tres = input()
if uno == dos and uno > tres:
    print (tres,",", dos,",", uno)
elif uno == tres and uno > dos:
    print (dos,",", tres,",", uno)
elif dos == tres and dos > uno:
    print (uno,",", dos,",", tres)
elif uno > dos and uno > tres and dos >= tres:
    print (tres,",", dos,",", uno)
elif dos > uno and dos > tres and uno >= tres:
    print (tres,",", uno,",", dos)
else:
    print (uno,",", dos,",", tres)



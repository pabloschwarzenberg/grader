#Descomponer un número
digitos=int(input("Ingrese 4 digitos: "))
digito=str(digitos)
if len(digito)==4:
    todo=digito[0]+"M + "+digito[1]+"C + "+digito[2]+"D + "+digito[3]+"U"
    print(todo)
elif len(digito)==3:
    todo=digito[0]+"C + "+digito[1]+"D + "+digito[2]+"U"
    print(todo)
elif len(digito)==2:
    todo=digito[0]+"D + "+digito[1]+"U"
    print(todo)
elif len(digito)==1:
    todo=digito[0]+"u"
    print(todo)
else:
    print("Fallo en los digitos")
#multiplos
numero_inicio=int(input("Ingrese primer valor: "))
numero_final=int(input("Ingrese termino final: "))
if(numero_inicio>=numero_final):
    print("Valores ingresados no validos")
else:
    while(numero_inicio<=numero_final):
        if(numero_inicio%2==0)or(numero_inicio%7==0):
            print(numero_inicio)
        numero_inicio=numero_inicio+1
 numero = eval(input("Ingrese un numero de hasta 4 cifras"))
valor_miles = (numero // 1000) % 10
valor_centenas = (numero // 100) % 10
valor_decenas = (numero // 10) % 10
valor_unidades = (numero // 1) % 10
numero = str(numero)
largo = len(numero)
if largo==1:
    print (valor_unidades,"U")
if largo==2:
    print (valor_decenas,"D +",valor_unidades,"U +",)
if largo==3:
    print (valor_centenas,"C +",valor_decenas,"D +",valor_unidades,"U")
if largo==4:
    print (valor_miles,"M +",valor_centenas,"C +",valor_decenas,"D +",valor_unidades,"U")          
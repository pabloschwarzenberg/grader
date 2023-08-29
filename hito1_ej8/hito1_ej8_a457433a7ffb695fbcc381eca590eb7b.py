numero = int(input("Ingresar un número de cuatro digitos: "))
unidades = numero%10
numero = numero // 10

decenas = numero%10
numero = numero//10

centenas = numero%10
numero = numero//10

unidadesMil = numero%10
print( str(unidadesMil)+'M'+'+'+str(centenas)+'C'+'+' + str(decenas)+'D'+'+'+ str (unidades)+'U')

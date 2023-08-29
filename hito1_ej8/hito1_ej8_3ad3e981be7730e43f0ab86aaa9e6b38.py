numero = int(input("\nIngrese un número de 4 dígitos: "))
auxiliar = numero
unidades = auxiliar%10
auxiliar = auxiliar//10
decenas = auxiliar%10
auxiliar = auxiliar//10
centenas = auxiliar%10
auxiliar = auxiliar//10
umil = auxiliar
print(umil,'M' '+',centenas,'C +',decenas,'D +',unidades,'U')
      
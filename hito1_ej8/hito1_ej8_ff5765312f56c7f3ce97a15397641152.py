## Entrada de datos:
numero = int(input("Ingresa un número de 4 cifras: "))
## Proceso:
unidades = numero%10
numero = numero//10
decenas = numero%10
numero = numero//10
centenas = numero%10
numero = numero//10
unidadesMil = numero%10
 print(f"\nDescomposición:{unidadesMil}M +{centenas}C+{decenas}D+{unidades}U\n")

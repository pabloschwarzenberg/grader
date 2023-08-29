#Descomponer un número
numero = int(input("ingrese el numero de 4 cifras"))
unidades = numero%10
numero = numero//10
decenas = numero%10
numero = numero//10
centenas = numero%10
numero = numero//10
unidadesmil = numero%10
print(f"M*{unidadesmil}+C*{centenas}+D*{decenas}+U*{unidades}")
n = int(input("seleccione el numero natural que representa los primeros numeros naturales, donde n es el ultimo natural: "))
sumatoria = (n * (n + 1)) / 2
if n >= 1:
    print("se hara el proceso de la suma, debido a que los naturales son enteros mayor o igual a 1")
    print("la suma es", sumatoria ,)
else:
     print("tal vez elegistes numeros racionales o el cero o los negativos, estimado")

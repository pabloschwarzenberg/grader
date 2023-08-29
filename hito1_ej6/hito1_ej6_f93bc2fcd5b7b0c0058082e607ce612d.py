#Ordenar tres números
nrouno = int (input("ingrese el primer numero: "))
nrodos = int (input("ingrese el segundo numero: "))
nrotres = int (input("ingrese el tercer numero: "))

a = min(nrouno, nrodos, nrotres)
c = max(nrouno, nrodos, nrotres)
b = (nrouno + nrodos + nrotres) - a - c

print("Los numeros son: {}, {}, {}".format(a, b, c))
      
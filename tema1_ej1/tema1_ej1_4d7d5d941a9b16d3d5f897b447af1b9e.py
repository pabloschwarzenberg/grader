#Suma de los N primeros números
n= int(input("Ingrese un numero : "))
n = n* (n + 1) / 2
format_float = "{:.0f}".format(n)
print (format_float)
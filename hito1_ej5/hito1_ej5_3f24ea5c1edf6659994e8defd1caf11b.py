#Cálculo del dígito verificador de un rut
#Entrada
print("Si su rut termina en k reemplácelo con un 0") 
rut = int(input("Ingrese su rut: "))
print("Su dígito verificador es: ", ((rut % 1000) % 100) % 10)      
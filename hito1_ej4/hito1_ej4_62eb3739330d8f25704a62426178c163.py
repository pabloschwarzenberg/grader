decimal = float(input("Ingrese un número decimal para convertir a binario: "))

#Operaciones 
if decimal <= 0:
    decimal = "0"
bin = ""
while decimal > 0: 
    resto = int(decimal % 2)
    decimal = int(decimal / 2)
    bin = str(resto) + bin

#Resultado 
print("resultado=", bin)
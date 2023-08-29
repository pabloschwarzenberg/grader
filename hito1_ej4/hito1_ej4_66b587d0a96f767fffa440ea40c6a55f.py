#Conversión de Decimal a Binario
#Entradas
num_deci = int(input("Ingresar el número decimal a transformar a binario: "))
resul = ""

#Ecuaciones
while num_deci != 0:
    resul = str(num_deci % 2) + resul
    num_deci //= 2

print("resultado = ", resul)

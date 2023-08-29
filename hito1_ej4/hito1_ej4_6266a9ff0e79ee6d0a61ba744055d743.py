#Conversión de Decimal a Binario
N = int(input("Ingrese numero decimal:")) 

Lista = []
while N>0:
   resto = int(N%2)
   Lista.append(resto)
   N = (N-resto)/2
   
n_bin = ""

for e in Lista[: :-1]:
  n_bin = n_bin + str(e)
  print("resultado="+str(n_bin))  
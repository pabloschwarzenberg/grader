#Conversión de Decimal a Binario
f = float(input("ingrese numero a binario"))
int32bits = np.asarray(f, dtype=np.float32).view(np.int32).item()
print(int32bits)
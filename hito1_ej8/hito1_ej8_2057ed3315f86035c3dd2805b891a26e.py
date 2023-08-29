print("descomponer un numero ")

n=float(input("ingrese un numero de cuatro cifras: "))

unidad=n%1
decena=n%10
centena=n%100
um= n%1000
print(f"\n al descomponer por unidad da como resultado ={round(unidad,2)}")
print(f"\n al descomponer por decena da como resultado  ={round(decena,2)}")
print(f"\n al descomponer por centena da como resultado={round(centena,2)}")
print(f"\n al descomponer por unidad de mil da como resultado={round(um,2)}")
#Descomponer un número
lista=[]
def string(data):
	for i in data:
		lista.append(int(i))
	print(lista)
numero=input("Ingrese un numero: ")
string(numero)

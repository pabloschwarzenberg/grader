listNumbers = []

while len(listNumbers) != 3:
    listNumbers.append(input("Favor ingrese un numero: "))

listNumbers.sort()

converted_list = [str(element) for element in listNumbers]
joined_string = ",".join(converted_list)


print("Lista de numeros:", joined_string)
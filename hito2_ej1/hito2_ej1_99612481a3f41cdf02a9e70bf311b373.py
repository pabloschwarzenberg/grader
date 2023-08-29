string1 = input("Ingrese la secuencia 1: ")
string2 = input("Ingrese la secuencia 2: ")

splitted_string1 = [x for x in string1]
splitted_string2 = [x for x in string2]

for i in range(len(splitted_string1)):
    if splitted_string1[i] != splitted_string2[i]:
        splitted_string2.insert(i, "_")


print("".join(splitted_string2))
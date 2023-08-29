#Descomponer un número
num = int(input("Ingrese numero  "))

num_to_list = [int(x) for x in str(num)]
num_to_list.reverse()

descom = ["U", "D", "C", "M"]
descom2 = descom[0:len(num_to_list)]

descom3 = []

for i in range(len(num_to_list) - 1, -1, -1):
    descom3.append(str(num_to_list[i])+descom2[i])

respuesta = ""
for x in descom3:
    respuesta = respuesta + x + " " + "+" + " "
print(respuesta[0: len(respuesta) - 2])
     
    
    
    
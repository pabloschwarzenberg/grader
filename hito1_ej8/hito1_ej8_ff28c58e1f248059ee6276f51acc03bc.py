#Descomponer un número
i = int(input("ingrese un numero : "))

w1 = int((i % 10000) / 1000)
w2 = int((i % 1000) / 100)
w3 = int((i % 100) / 10)
w4 = i % 10

print(w1,"M","+",w2,"C","+",w3,"D","+",w4,"U")

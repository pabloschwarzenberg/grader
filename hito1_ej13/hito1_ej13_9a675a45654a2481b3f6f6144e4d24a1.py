x = 2
n = eval(input("Ingrese un número entero: "))

while(n != 1):
    if(n% x == 0):
      print(str(x) + " ")
      n = n // x

    else:
        x = x + 1
      
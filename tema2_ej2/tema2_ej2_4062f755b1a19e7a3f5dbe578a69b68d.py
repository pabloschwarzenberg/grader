# completa el código de la función
a = int(input (220))
b = int(input (280))
def numeros(a, b):
                 suma_a = 0
                 suma_b = 0
                 for i in range (1, a):
                                      if a % i == 0:
                                                    suma_a += i
                 for j in range (1, b):
                                      if (b % j == 0): #amigos
                                                    suma_b += j
                 return suma_a == b and suma_b == a
                 if numeros (a, b): print ("True")
                 else: print ("False")
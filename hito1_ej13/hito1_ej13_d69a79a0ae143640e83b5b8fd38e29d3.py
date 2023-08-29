def descomponer (numero):
     primos = []
     for i in range (2, numero+1):
         while numero % i == 0:
             primos.append(i)
             numero= numero/i
     p = ""
     for i in primos:
         p += str(i) + "\n"
     return p
#ordenar 3 numeros

primerNumero = int(input("Ingrese el primer numero"))
segundoNumero = int(input("Ingrese el segundo numero"))
tercerNumero = int(input("Ingrese el tercer numero"))


a = min(primerNumero, segundoNumero, tercerNumero)
c = max(primerNumero, segundoNumero, tercerNumero)
b = (primerNumero + segundoNumero + tercerNumero)- a - c


print(a,"," ,  b , ",", c)
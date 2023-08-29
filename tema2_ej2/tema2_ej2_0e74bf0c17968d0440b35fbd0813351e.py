# completa el código de la función
def amigos(a,b):
  return
      
#Ingreso de datos y operacion

def son_amigos(a, b):
    def calcular_divisores(numero):
        divisores = []
        for i in range(1, numero):
            if numero % i == 0:
                divisores.append(i)
        return divisores

    suma_divisores_a = sum(calcular_divisores(a))
    suma_divisores_b = sum(calcular_divisores(b))

    return suma_divisores_a == b and suma_divisores_b == a

#Respuesta
print(son_amigos(1, 2))
print(son_amigos(4, 4))
print(son_amigos(220, 284))
print(son_amigos(1184, 1210))

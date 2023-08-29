# completa el código de la función
def suma_divisores(a):
 div_a =0 
 if a < 1:
   print("El numero ingresado no es valido")
 else: 
    for i in range (1, a): 
        if a%i==0:
            div_a +=i

    if a == 0 or a == 1 or a == 4:
       return div_a, False
    for x in range (2, int(a/2)):
       if a % x == 0: 
           return div_a, False
    return div_a, True 

if __name__ == "__main__" :
  num=int(input("ingrese un numero: "))
  print(suma_divisores(num))
           
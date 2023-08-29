# completa el código de la función
def amigos (a,b):
    div1 = 1
    div2 = 1
    sum1 = 0
    sum2 = 0
    while div1 < a:
       if a%div1 == 0:
            sum1 += div1
       div1 += 1
    while div2 < b:
        if b%div2 == 0:
            sum2+=div2
        div2 += 1
    if sum1 == b and sum2 == a:
       return True
    else:
       return False
try:
    num1 = int(input("Numero 1: "))
    num2 = int(input("Numero 2: "))
    print(amigos(num1,num2))
except:
    print("ERROR: Ingrese otro numero")
# completa el código de la función
def amigos(a,b):
    div_a=1
    div_b=1
    sum_a=0
    sum_b=0
    while div_a<a:
        if a%div_a==0:
            sum_a+=div_a
            #print("Div de a:", div_a)
            #print("Sumaa", sum_a)
        div_a+=1
    while div_b<b:
        if b%div_b==0:
            sum_b+=div_b
            #print("Div de b:", div_b)
            #print("Sumab", sum_b)
        div_b += 1
    if sum_a==b and sum_b==a:
        return True
    else:
        return False

# num1 = int(input("Número 1: "))
# num2 = int(input("Número 2: "))
# print(amigos(num1,num2))
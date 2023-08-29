def suma_div(number):
    div=[]
    for i in range(1,number):
        if number%i==0:
            div.append(i)
    return sum(div)

def amigos(a,b):
    if suma_div(a)==b and suma_div(b)==a:
        return True
    else:
        return False

if __name__ == "__main__":
    num1=int(input("Primer número: "))
    num2=int(input("Segundo número: "))
    print(amigos(num1,num2))
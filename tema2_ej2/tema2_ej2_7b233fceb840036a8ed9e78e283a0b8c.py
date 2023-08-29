# completa el código de la función
def amigos(num1,num2):
    div_a=1
    div_b=1
    for d in range(2,num1):
        if num1%d==0:
            div_a=div_a+d
    for f in range(2,num2):
        if num2%f==0:
            div_b=div_b+f
    if num1==2 or num2==2:
        if num1==2:
            div_a=div_a+2
        if num2==2:
            div_b=div_b+2
    if div_a==num2 or div_b==num1:
        return (True)
    else:
        return(False)
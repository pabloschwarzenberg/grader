#Factores Primos
num=int(input('numero:'))
div=1
a=0
b=2
d=0
while num>=div:
    a=num%div
    if a==0:
        while div>=b:
            if div==b:
                print (div)
                num=num/div
                b=2
                div=1
                break
            d=div%b
            if d==0 and div!=b:
                break
            elif div==b:
                print(div)
                num=num/div
                b=2
                div=1
                break
            elif d!=0 and div!=b:
                b=b+1
        b=2
    div=div+1
      
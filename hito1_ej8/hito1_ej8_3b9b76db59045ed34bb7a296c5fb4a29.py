#Descomponer un número
x=int(input('Ingrese un número hasta 4 cifras: '))

if 0<=x<=9:
    cadenaderespuesta=str(x)+'U'
    print(cadenaderespuesta)
elif 10<=x<=99:
    d1=x%10
    x=x//10

    d2=x%10
    cadenaderespuesta= str(d2)+'D + '+str(d1)+'U'
    print(cadenaderespuesta)
elif 100<=x<=999:
    d1=x%10
    x=x//10

    d2=x%10
    x=x//10

    d3=x%10
    cadenaderespuesta= str(d3)+'C + '+str(d2)+'D + '+str(d1)+'U'
    print(cadenaderespuesta)
elif 1000<=x<=9999:
    d1=x%10
    x=x//10

    d2=x%10
    x=x//10

    d3=x%10
    x=x//10

    d4=x%10

    cadenaderespuesta= str(d4)+'M + '+str(d3)+'C + '+str(d2)+'D + '+str(d1)+'U'
    print(cadenaderespuesta)
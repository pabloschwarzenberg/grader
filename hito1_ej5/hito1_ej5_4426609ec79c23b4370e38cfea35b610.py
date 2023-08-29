#Cálculo del dígito verificador de un rut
rut = int(input("ingrese rut="))
ruce = str(rut)
largo = len(ruce)
i=1
j=2
sum=0
while i <= largo:
    num=int(ruce[largo-i:largo-i+1])
    if(j > 7):
        j=2

    sum = sum+num*j
    j = j+1
    i = i+1
digito=(11-(sum-(int(sum/11))*11))
if(digito < 10):

    print("dv=" + str(digito))
else:
    if(digito==11):
        print("dv=0")
    else:
        print("dv=K")
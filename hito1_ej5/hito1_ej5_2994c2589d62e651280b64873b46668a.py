r = int(input("Ingrese el rut sin el digito verficador: "))

d1 = r%10
r = r//10

d2 = r%10
r = r//10

d3 = r%10
r = r//10

d4 = r%10
r = r//10

d5 = r%10
r = r//10

d6 = r%10
r = r//10

d7 = r%10
r = r//10

d8 = r%10
r = r//10

formula = d1*2 + d2*3 + d3*4 + d4*5 + d5*6 + d6*7 + d7*2 + d8*3
resto = formula%11
resta = 11 - resto

if resta == 11:
    print("dv=0")
if resta == 10:
    print("dv=K")
if resta !=11 and resta !=10:
    print("dv=",resta)

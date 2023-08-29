"""
Escribe un programa que resuelva un sistema de dos ecuaciones con dos incognitas. 
Tu programa recibirá los seis números reales que representan el sistema 
y deberá imprimir la dos soluciones redondeadas a un decimal. 
Ejemplo: Para el sistema 2x+3y=6 y x+2y=5, tu programa debe imprimir
"""

a=int(input("escriba numero a: "))
b=int(input("escriba numero b: "))
c=int(input("escriba numero c: "))
d=int(input("escriba numero d: "))
e=int(input("escriba numero e: "))
f=int(input("escriba numero f: "))


x=(((b*f)-(c*e))/((b*d)-(a*e)))
y=((c-(a*(((b*f)-(c*e))/((b*d)-(a*e)))))/b)

print("x=",x)
print("y=",y)
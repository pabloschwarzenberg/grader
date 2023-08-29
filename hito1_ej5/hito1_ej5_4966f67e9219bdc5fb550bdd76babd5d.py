rut = input("Ingrese su rut(sin codigo verificador): ")

tamano = len(rut) - 1
producto = 0
valor = 2 
producto = int(rut[tamano]) * valor
while (tamano > 0):
    valor += 1
    tamano -= 1
    producto = producto + (int(rut[tamano]) * valor)
    if valor == 7:
        valor = 1
        
modulo = producto // 11
resto = producto - ( 11 * modulo)
final = 11 - resto

if final == 11:
    print("dv=0")
elif final == 10:
    print("dv=K")
else:
    print( "dv=",final )


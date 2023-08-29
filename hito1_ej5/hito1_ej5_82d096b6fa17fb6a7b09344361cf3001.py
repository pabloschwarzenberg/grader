#Programa para calcular el dígito verificador de un rut
rut = str (input("Ingresa el RUT sin codigo verificador: "))

if len(rut) == 7:
    dig2 = 2 * int(rut[6])
    dig3 = 3 * int(rut[5])
    dig4 = 4 * int(rut[4])
    dig5 = 5 * int(rut[3])
    dig6 = 6 * int(rut[2])
    dig7 = 7 * int(rut[1])
    dig8 = 2 * int(rut[0])
    diga = dig2 + dig3 + dig4 + dig5 + dig6 + dig7 + dig8
    once = 11
    digb = diga / once
    digc = once * int(digb)
    digd = diga - digc
    dv = 11 - digd

elif len(rut) == 8:
    dig1 = 2 * int(rut[7])
    dig2 = 3 * int(rut[6])
    dig3 = 4 * int(rut[5])
    dig4 = 5 * int(rut[4])
    dig5 = 6 * int(rut[3])
    dig6 = 7 * int(rut[2])
    dig7 = 2 * int(rut[1])
    dig8 = 3 * int(rut[0])
    diga = dig1 + dig2 + dig3 + dig4 + dig5 + dig6 + dig7 +dig8
    once = 11
    digb = diga / once
    digc = once * int(digb)
    digd = diga - digc
    dv = 11 - digd

if dv < 10:
    print ("dv=" + str(dv))
elif dv == 10:
    print ("dv=k" )
elif dv == 11:
    print ("dv= 0")

#dijito verifucador

n_documento = []
print(str("----------------- Calculo del digito Vrificador de su RUT ------------------"))
print(str("------- Favor ingresar su N° de RUT sin puntos ni digito verificador -------"))
RUT = input("RUT: ")
n_documento.append(RUT)
n_doc = n_documento[0]
adi = 0
a = len(n_doc)
b = 2
c = 0
d = a - 1
e = a
while c < a:
    num = int(n_doc[d:e]) * b
    c = c + 1
    b = b + 1
    d = d - 1
    e = e - 1
    if b == 8:
        b = 2
    adi = adi + num

pas = (adi // 11)
sust = adi - (11 * pas)
verif = 11 - sust
if verif < 10:
    print("dv=%d" %(verif))
if verif == 11:
    verif = 0
    print("dv=%d" %(verif))
if verif == 10:
    verif = "K"
    print("dv=%s" %(verif))
    print("dv=%s" %(verif))
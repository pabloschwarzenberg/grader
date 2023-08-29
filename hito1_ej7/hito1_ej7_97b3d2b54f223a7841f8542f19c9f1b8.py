from datetime import datetime
fecha=input("ingresar fecha de nacimiento: ")
x = datetime.strptime(fecha, '%d%m')
fecha_inicial_aries="2103"
fecha_final_aries="2004"
fecha_inicial_taurus="2104"
fecha_final_taurus="2005"
fecha_inicial_gemini="2105"
fecha_final_gemini="2106"
fecha_inicial_cancer="2206"
fecha_final_cancer="2207"
fecha_inicial_leo="2307"
fecha_final_leo="2208"
fecha_inicial_virgo="2308"
fecha_final_virgo="2209"
fecha_inicial_libra="2309"
fecha_final_libra="2210"
fecha_inicial_escorpio="2310"
fecha_final_escorpio="2211"
fecha_inicial_sagitario="2311"
fecha_final_sagitario="2212"
fecha_inicial_capricorn="2312"
fecha_final_capricorn="2001"
fecha_inicial_aquarius="2101"
fecha_final_aquarius="1902"
fecha_inicial_piscies="2002"
fecha_final_piscies="2003"

fia = datetime.strptime(fecha_inicial_aries, '%d%m')
ffa = datetime.strptime(fecha_final_aries, '%d%m')
fit= datetime.strptime(fecha_inicial_taurus, '%d%m')
fft = datetime.strptime(fecha_final_taurus, '%d%m')
fig = datetime.strptime(fecha_inicial_gemini, '%d%m')
ffg = datetime.strptime(fecha_final_gemini, '%d%m')
fic = datetime.strptime(fecha_inicial_cancer, '%d%m')
ffc = datetime.strptime(fecha_final_cancer, '%d%m')
fil = datetime.strptime(fecha_inicial_leo, '%d%m')
ffl = datetime.strptime(fecha_final_leo, '%d%m')
fiv = datetime.strptime(fecha_inicial_virgo, '%d%m')
ffv = datetime.strptime(fecha_final_virgo, '%d%m')
fili = datetime.strptime(fecha_inicial_libra, '%d%m')
ffli = datetime.strptime(fecha_final_libra, '%d%m')
fie = datetime.strptime(fecha_inicial_escorpio, '%d%m')
ffe = datetime.strptime(fecha_final_escorpio, '%d%m')
fis = datetime.strptime(fecha_inicial_sagitario, '%d%m')
ffs = datetime.strptime(fecha_final_sagitario, '%d%m')
fica = datetime.strptime(fecha_inicial_capricorn, '%d%m')
ffca = datetime.strptime(fecha_final_capricorn, '%d%m')
fiaq = datetime.strptime(fecha_inicial_aquarius, '%d%m')
ffaq = datetime.strptime(fecha_final_aquarius, '%d%m')
fip = datetime.strptime(fecha_inicial_piscies, '%d%m')
ffp = datetime.strptime(fecha_final_piscies, '%d%m')


if fia<=x<=ffa:
    print("aries")
if fit<=x<=fft:
    print("tauro")
if fig<=x<=ffg:
    print("geminis")
if fic<=x<=ffc:
    print("cancer")
if fil<=x<=ffl:
    print("leo")
if fiv<=x<=ffv:
    print("virgo")
if fie<=x<=ffe:
    print("escorpio")
if fis<=x<=ffs:
    print("sagitario")
if fica<=x<=ffca:
    print("capricornio")
if fiaq<=x<=ffaq:
    print("aquarius")
if fip<=x<=ffp:
    print("piscis")
if fili<=x<=ffli:
    print("libra")
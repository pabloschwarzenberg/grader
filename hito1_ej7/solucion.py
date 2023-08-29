signos=[
    ["aries",21,3,20,4],
    ["tauro",21,4,21,5],
    ["geminis",22,5,21,6],
    ["cancer",22,6,22,7],
    ["leo",23,7,22,8],
    ["virgo",23,8,23,9],
    ["libra",24,9,23,10],
    ["escorpio",24,10,22,11],
    ["sagitario",23,11,21,12],
    ["capricornio",22,12,20,1],
    ["acuario",21,1,19,2],
    ["piscis",20,2,20,3]
]

def encontrar_signo(dia,mes):
    for signo in signos:
        if mes==signo[2] or mes==signo[4]:
            if mes==signo[2] and dia>=signo[1]:
                return signo[0]
            if mes==signo[4] and dia<=signo[3]:
                return signo[0]
    return "error"

dia=int(input())
mes=int(input())
print(encontrar_signo(dia,mes))
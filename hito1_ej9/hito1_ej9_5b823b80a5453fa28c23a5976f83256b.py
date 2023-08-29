#Sistema de Ecuaciones
ecuacion1 = input("Ecuación 1: ")
ecuacion2 = input("Ecuación 2: ")
#ecuacion1 = "2x+3y=6" #hacerlo input
#ecuacion2 = "x+2y=5" #hacerlo input

def AxByC(ecuacion):
    #ax + by + c = 0
    ax = 0
    by = 0
    c = 0
    ec = ecuacion

    if "x" in ecuacion:
        ec = ecuacion.split("x")
        if ec[0] != "":
            ax = int(ec[0])
        else:
            ax = 1

        if "y" in ec[1]:
            ec = ec[1].split("y")
            if ec[0] != "":
                by = int(ec[0])
            else:
                by = 1

    if "y" in ecuacion:
        ec = ecuacion.split("y")
        if ec[0] != "":
            by = int(ec[0])
        else:
             by = 1
    
    ec = ecuacion.split("=")
    c = int(ec[1])*(-1)

    return [ax,by,c]      

def resultadoY(ec1, ec2):
    ax1 = ec1[0]
    by1 = ec1[1]
    c1 = ec1[2]
    ax2 = ec2[0]
    by2 = ec2[1]
    c2 = ec2[2]

    y = (ax2*c1 - ax1*c2) / (ax1*by2 - ax2*by1)
    return y

def resultadoX(ec1, y):
    ax = ec1[0]
    by = ec1[1]
    c = ec1[2]

    x = (c*(-1) - by*y) / ax
    return x

abc1 = AxByC(ecuacion1)
abc2 = AxByC(ecuacion2)

Y = resultadoY(abc1, abc2)
X = resultadoX(abc1, Y)

X = int(X*10)/10
Y = int(Y*10)/10

print("x=" + str(X))
print("y=" + str(Y))
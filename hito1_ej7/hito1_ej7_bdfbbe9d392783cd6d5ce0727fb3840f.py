dia = int(input())
mes = int(input())

if(mes == 3 and dia >= 21) or (mes == 4 and dia <= 20):
    print("aries")
if(mes == 4 and dia >= 21) or (mes == 5 and dia <= 21):
    print("tauro")
if(mes == 5 and dia >= 22) or (mes == 6 and dia <= 22):
    print("geminis")
if(mes == 6 and dia >= 23) or (mes == 7 and dia <= 23):
    print("leo")
if(mes == 8 and dia >= 24) or (mes == 9 and dia <= 23):
    print("virgo")
if(mes == 9 and dia >= 24) or (mes == 10 and dia <= 23):
    print("libra")
if(mes == 10 and dia >= 24) or (mes == 11 and dia <= 22):
    print("escorpio")
if(mes == 11 and dia >= 23) or (mes == 12 and dia <= 21):
    print("sagitario")
if(mes == 12 and dia >= 22) or (mes == 1 and dia <= 20):
    print("capricornio")
if(mes == 1 and dia >= 21) or (mes == 2 and dia <= 18):
    print("acuario")
if(mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
    print("piscis")
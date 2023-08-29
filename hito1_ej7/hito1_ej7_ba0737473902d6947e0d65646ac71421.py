dia= int(input("escribe el dia de tu nacimiento:"))
mes= int(input("escribe el mes de tu nacimiento:"))

def main():
    if (20<=dia<=31 and mes==3) or (1<=dia<21 and mes==4):
        print("Aries")
    if (21<=dia<=31 and mes==4) or (1<=dia<22 and mes==5):
        print("Tauro")
    if (22<=dia<=31 and mes==5) or (1<=dia<=21 and mes==6):
        print("Gemini")
    if (22<=dia<=31 and mes==6) or (1<=dia<=22 and mes==7):
        print("Cancer")
    if (23<=dia<=31 and mes==7) or (1<=dia<=22 and mes==8):
        print("leo")
    if (23<=dia<=31 and mes==8) or (1<=dia<=23 and mes==9):
        print("virgo")
    if (24<=dia<=31 and mes==9) or (1<=dia<=23 and mes==10):
        print("Libra")
    if (24<=dia<=31 and mes==10) or (1<=dia<=22 and mes==11):
        print("Scorpius")
    if (23 <= dia <= 31 and mes == 11) or (1 <= dia <= 21 and mes == 12):
        print("Sagitarius")
    if (22<=dia<=31 and mes==12) or (1<=dia<=20 and mes==1):
        print("Capricornio")
    if (21<=dia<=31 and mes==1) or (1<=dia<=19 and mes==2):
        print("Aquarius")
    if (20<=dia<=31 and mes==2) or (1<=dia<=20 and mes==3):
        print("Pisces")

main()
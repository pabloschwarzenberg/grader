__author__ = 'matias'
def jeringozo(string):
    traducida=""
    for letra in string:
        if letra=="a":
            traducida+="apa"
        if letra=="e":
            traducida+="epe"
        if letra=="i":
            traducida+="ipi"
        if letra=="o":
            traducida+="opo"
        if letra=="u":
            traducida+="upu"

        if letra!="a" and letra!="e" and letra!="i" and letra!="o" and letra!="u":
            traducida+=letra

    return traducida
if __name__ == "__main__":
  testo=input("ingrese texto para traducir a jerigonzo:")
  print ( jeringozo(testo))
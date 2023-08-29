def jerigonzo(string):
  nuevapalabra=""
  for vocal in string:
    if vocal=="a":
        nuevapalabra+="apa"
    elif vocal=="e":
        nuevapalabra+="epe"
    elif vocal=="i":
        nuevapalabra+="ipi"
    elif vocal=="o":
        nuevapalabra+="opo"
    elif vocal=="u":
        nuevapalabra+="upu"
    elif vocal=="A":
        nuevapalabra+="Apa"
    elif vocal=="E":
        nuevapalabra+="Epe"
    elif vocal=="I":
        nuevapalabra+="Ipi"
    elif vocal=="O":
        nuevapalabra+="Opo"
    elif vocal=="U":
        nuevapalabra+="Upu"
    else:
        nuevapalabra+= vocal
  return nuevapalabra    

if __name__ == "__main__":
  string=input()
  nuevapalabra=(string)
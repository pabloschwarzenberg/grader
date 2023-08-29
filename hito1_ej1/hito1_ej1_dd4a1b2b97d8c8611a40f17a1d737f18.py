#Nota final
PT=float(input(""))
PI=float(input(""))
NE=float(input(""))
PP=float(input(""))
if 0<=PT<=7.0 and 0<=PI<=7.0 and 0<=NE<=7.0 and 0<=PP<=7.0:
    print(round(0.3*PT+0.3*PI+0.3*NE+0.1*PP,1))
else:
    0>PT>7.0 or 0>PI>7.0 or 0>NE>7.0 or 0>PP>7.0
    print("No concuerda")

      
t=input("número de celular que llama: ")
t=int(t)
h=input("hora del día: ")
h=int(h)

if 0<h<7:
    print("CONTESTAR")
elif 7<h<14 and (t%1000)==909:
    print("CONTESTAR")
elif 17<h<19 and t//100000!=877:
    print("CONTESTAR")
else:
    print("NO CONTESTAR")

      
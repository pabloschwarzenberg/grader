inp_=str(input())
asd="+"
if len(inp_)==1:
    print(inp_[-1::4] + "U")
elif len(inp_)==2:
    print(inp_[-2::4] + "D" + asd + inp_[-1::4] + "U" )
elif len(inp_)==3:
    print(inp_[-3::4] + "C" + asd + inp_[-2::4] + "D" + asd + inp_[-1::4] + "U")
elif len(inp_)==4:
    print(inp_[-4::4] + "M" + asd + inp_[-3::4] + "C" + asd + inp_[-2::4] + "D" + asd + inp_[-1::4] + "U")


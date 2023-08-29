# Cajero Automático
s_i = 1000000
b_i = [20, 40, 40]
v_b = [20000, 10000, 5000]
s_c = 100000
i = 0
u = int(input())
while (i < 3 or c == "N"):
    c = str(input("Clave: "))
    if c != "1803" or u != 10334151:
        print("clave invalida o usuario invalido.")
        i = i + 1
    elif c == "1803":
        m_r = int(input("Monto a retirar: "))
        if m_r > 100000 or m_r <= 0:
            print("monto no permitido o invalido.")
        else:
            s_i = s_i - m_r
            s_c = s_c - m_r
            b_20 = m_r//v_b[0]
            m_r = m_r-b_20*20000
            b_10 = m_r // v_b[1]
            m_r = m_r - b_10 * 10000
            b_5 = m_r // v_b[2]
            m_r = m_r - b_5 * 5000
        break
print("saldo cuenta={}".format(s_c))
print("saldo cajero={}".format(s_i))
print("billetes 20000={}".format(b_20))
print("billetes 10000={}".format(b_10))
print("billetes 5000={}".format(b_5))
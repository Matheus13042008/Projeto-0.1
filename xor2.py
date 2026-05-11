A = False
B = False
C = False
D = False

valores = {True, False}
for A in valores:
    for B in valores:
        for C in valores:
            for D in valores:
                regra =(((not((not C) and A)) or (B or D)) and ((not D) and C))
                print(A ,B ,C ,D,'VAI DÁ:', regra)

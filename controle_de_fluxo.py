x1 = int(input('Entre com o x1:\n'))
y1 = int(input('Entre com o y1:\n'))
w1 = int(input('Entre com o w1:\n'))
h1 = int(input('Entre com o h1:\n'))

x2 = int(input('Entre com o x2:\n'))
y2 = int(input('Entre com o y2:\n'))
w2 = int(input('Entre com o w2:\n'))
h2 = int(input('Entre com o h2:\n'))

intersecta_em_x = (x2+w2 >= x1 and x2 <= x1) or (x2+w2 <= x1+w1 and x2 >= x1 ) or (x2 >= x1 and x2 <= x1+w1)
não_intersecta_em_x = (x2+w2 < x1) or (x2 > x1+w1)

intersecta_em_y = (y2+h2 >= y1) or (y2 >= y1 and y2+h2 <= y1+h1) or (y2 <= y1+h1 and y2+h2 >= y1+h1)
não_intersecta_em_y = (y2 > y1 + h1) or (y2+h2 < y1)

if intersecta_em_x and intersecta_em_y:
    print('Está intersectando no Segundo Polígono')
else:
    print('Não Está intersectando no Segundo Polígono')




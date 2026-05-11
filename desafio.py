x1 = input('Qual o x1:')
y1 = input('Qual o y1:')
h1 = input('Qual o h1:')
w1 = input('Qual o w1:')
'''
x1, y1
x1,y1 + h1
x1 + w1, y1
x1 + w1, y1 + h1

'''

x2 = input('Qual o x2:')
y2 = input('Qual o y2:')
h2 = input('Qual o h2:') 
w2 = input('Qual o w2:')

não_cruza_em_y = (y2 + h2 < y1) or (y2 > y1+h1)
cruza_em_y = (y2+h2 >= y1 and y2+h2 <= y1+h1) or (y2 >= y1 and y2 <= y1+h1)

não_cruza_em_x = (x2 + w2 < x1) or (x2 > x1+w1)
cruza_em_x = (x2+w2 >= x1 and x2+w2 <= x1+w1) or (x2 >= x1 and x2 <= x1 + w1)

if cruza_em_y and cruza_em_x:
    print('Estao cruzando')
else:
    print('Não estão cruzando')

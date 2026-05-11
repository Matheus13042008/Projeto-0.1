a = int(input('Entre com o valor de a: \n'))
b = int(input('Entre com o valor de b: \n'))

print(f'a == b: {a == b}')
print(f'a != b: {a != b}')
print(f'a >= b: {a >= b}')
print(f'a > b: {a > b}')
print(f'a <= b: {a <= b}')
print(f'a < b: {a < b}')

condicao = (a >= b) or (a != b)
if condicao:
    print('Executou o if da condição')
else:
    print('Executou o else da condição')


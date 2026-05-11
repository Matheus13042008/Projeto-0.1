idade = int(input('Qual sua Idade?\n'))
ano = int(input('Quando você nasceu?\n'))
peso = float(input('Qual seu peso?\n'))
altura = float(input('Qual sua altura?\n'))


print('Seu IMC é:', peso / altura**2)

resto = idade % 7
if resto == 0:
    print('Sua idade é divisivel por 7\n')
else:
    print('Sua idade não é divisivel por 7\n')

resto2 = ano % 4
if resto2 == 0:
    print('Você nasceu em ano bissexto')
else:
    print('Você não nasceu em ano bissexto')
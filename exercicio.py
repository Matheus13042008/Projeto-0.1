genero = input('Qual seu genero: \n')
idade = int(input('Qual sua idade: \n'))
compra = float(input('Qual o valor da compra: \n'))
VIP = input('Tem VIP(S/N): \n')

desconto = 0
if idade > 70:
    desconto = desconto + 15
if idade >= 50 and idade <= 70:
    desconto = desconto + 10
if idade >= 30 and idade < 50:
    desconto = desconto + 5
if VIP == 'S':
    desconto = desconto + 5
if compra >= 500:
    desconto = desconto + 5
    print('O percentual de desconto é', desconto)
    valor_liquido = compra - compra*desconto/100
    print('o valor de pagamento é de:', valor_liquido)


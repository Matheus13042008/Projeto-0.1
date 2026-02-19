nome = input('Qual o seu nome:\n')
print('Ola',nome,' Seja bem vindo')
senha = input('Qual sua senha:\n')
print('Sua senha é:\n',senha)
dominio =input('Qual seu dominio:\n')
print('O seu dominio é:\n',dominio)

email = nome + '@' + dominio 
print('Seu email é:\n',email)

palavra = 'jaca'
#colocar a string como toda maiuscula
print('Colocando o texto em maiuscula:',palavra.upper())
PALAVRA = 'JACA'
print('Palavra em Minuscula:', PALAVRA.lower())

contagem = email

print('SUA NOVA SENHA É:','a' + str(contagem.count('a')) + 'e' + str(contagem.count('e')) + 'i' + str(contagem.count('i')) + 'o' + str(contagem.count('o')) + 'u' + str(contagem.count('u')))




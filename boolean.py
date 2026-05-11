

var_1 = True
var_2 = False

print('var_1 {} quando negada fica {}'.format(var_1, not var_1))
print('var_2 {} quando negada fica {}'.format(var_2, not var_2))

'''
Logica do AND (E)
'''

var_1_t = True
var_1_f = False
var_2_t = True
var_2_f = False

print('Quando var_1_t é {} E var_2_t {} o resultado é {}'.format(var_1_t,var_2_t,var_1_t and var_2_t))
print('Quando var_1_f é {} E var_2_t {} o resultado é {}'.format(var_1_f,var_2_t,var_1_f and var_2_t))
print('Quando var_1_t é {} E var_2_f {} o resultado é {}'.format(var_1_t,var_2_f,var_1_t and var_2_f))
print('Quando var_1_f é {} E var_2_f {} o resultado é {}'.format(var_1_f,var_2_f,var_1_f and var_2_f))


''' 
Logica do OR
'''

print('Quando var_1_t é {} OU var_2_t {} o resultado é {}'.format(var_1_t,var_2_t,var_1_t or var_2_t))
print('Quando var_1_f é {} OU var_2_t {} o resultado é {}'.format(var_1_f,var_2_t,var_1_f or var_2_t))
print('Quando var_1_t é {} OU var_2_f {} o resultado é {}'.format(var_1_t,var_2_f,var_1_t or var_2_f))
print('Quando var_1_f é {} OU var_2_f {} o resultado é {}'.format(var_1_f,var_2_f,var_1_f or var_2_f))

'''
Multiplas regras de logica
'''

var_1_t = True
var_1_f = True
var_2_t = True
var_2_f = True

var_resultado = ((var_1_t and var_2_f) or ((var_1_t or var_2_t) and (not var_2_f)))
print('O resultado da logica é {}'.format(var_resultado))
'





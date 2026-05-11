A = bool(input())
B = bool(input())

A = False
B = False
regra = ((not A) and B) or ((not B) and A)
print(A, B, regra)

A = False
B = True
regra = ((not A) and B) or ((not B) and A)
print(A, B, regra)

A = True
B = False
regra = ((not A) and B) or ((not B) and A)
print(A, B, regra)

A = True
B = True
regra = ((not A) and B) or ((not B) and A)
print(A, B, regra)




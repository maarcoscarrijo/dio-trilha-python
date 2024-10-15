# Operador de identidade, é o operador: is (de "É" em English)

curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

identity_1 = curso is nome_curso
print(identity_1)

identity_2 = curso is not nome_curso
print(identity_2)

identity_3 = saldo is limite
print(identity_3)

identity_4 = saldo is not limite
print(identity_4)
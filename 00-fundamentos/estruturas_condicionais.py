saldo = 2000.0
saque = float(input("Informe o valor para o saque: "))

if saldo >= saque:
    saldo = saldo - saque
    print(f"Saque realizado, seu saldo atualizado é: {saldo}")

else:
    print("Saldo insuficiente para este saque!")


    ##

MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Já tem idade para tirar CNH!")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas.") ## Não é realidade, somente para teste else if
else:
    print("Ainda não tem idade para tirar CNH.")
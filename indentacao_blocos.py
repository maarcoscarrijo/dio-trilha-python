def sacar(valor):
    saldo = 500
    if saldo >= valor:
        print("Sacou!")

def depositar(valor):
    saldo = 500
    saldo = saldo + valor
    print(saldo)

    
    
sacar(100)
depositar(300)

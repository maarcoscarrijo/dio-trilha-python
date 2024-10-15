def celcular_total(numeros):
    return sum(numeros)


def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor


def func_3():
    print("Olá mundo!")


print(celcular_total([10, 20, 30, 4]))
print(retorna_antecessor_e_sucessor(10))
print(func_3()) # Não passado um atributo e um return válido, retorna None, como se tivesse passado na função: return None;
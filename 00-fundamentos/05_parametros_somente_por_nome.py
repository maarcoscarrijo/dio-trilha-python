def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    # salvar carro no banco de dados...
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro(modelo="Palio", ano=1994, placa="CCJ-8242", marca="Fiat", motor="1.5", combustivel="Gasolina") # Válido
# criar_carro("Palio", 1994, "CCJ-8242", marca="Fiat", motor="1.5", combustivel="Gasolina") # inválido
# criar_carro("Palio", 1994, "CCJ-8242", "Fiat", "1.5", "Gasolina") # inválido
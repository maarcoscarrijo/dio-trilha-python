def salvar_carro(marca, modelo, ano, placa):
    # salvar carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Fiat", "Palio", 1996, "CCJ-8242") # passando lista nas posições corretas, porém pode gerar erro se mudar as posições dos arqumentos.
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234") # Forçando os elementos
salvar_carro(**{"marca" : "Fiat", "modelo": "Strada", "ano": 2001, "placa": "ABC-7890"}) # Passando dicionário (kwargs)
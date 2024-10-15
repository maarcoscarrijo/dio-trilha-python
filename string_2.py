## Concatenando String

# Old style %

nome = "Marcos"
idade = 30
profissao = "Desenvolvedor"
linguagem = "Python e Java"

dados = {"nome" : "Marcos", "idade" : 30, "profissao" : "Desenvolvedor", "linguagem" : "Python e Java"}

print("Olá, me chamo %s. \nEu tenho %d anos de idade. \nTrabalho como %s. \nE estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))
print()

# Método format
print("Olá, me chamo {}. \nEu tenho {} anos de idade. \nTrabalho como {}. \nE estou matriculado no curso de .".format(nome, idade, profissao, linguagem))

print()

print("Olá, me chamo {3}. \nEu tenho {2} anos de idade. \nTrabalho como {1}. \nE estou matriculado no curso de {0}.".format(linguagem, profissao, idade, nome))

print()

print("Olá, me chamo {name}. \nEu tenho {age} anos de idade. \nTrabalho como {profissao}. \nE estou matriculado no curso de {linguage}.".format(age=idade, name=nome, profissao=profissao, linguage=linguagem))

print()

print("Olá, me chamo {nome}. \nEu tenho {idade} anos de idade. \nTrabalho como {profissao}. \nE estou matriculado no curso de {linguagem}.".format(**dados))

print()

# Método f-string
print(f"Olá, me chamo {nome}. \nEu tenho {idade} anos de idade. \nTrabalho como {profissao}. \nE estou matriculado no curso de {linguagem}.")

print()

# Formatar strings com o f-string

PI = 3.14159

print(f"Valor de PI: {PI:.2f}")

print(f"Valor de PI: {PI:10.2f}")


print(11 + 10 + 1258456) ## int = inteiro
print(1.5 + 0.5 + 5) ## float = pontos flutuantes
print(True) ## bool = Boleano
print(False) ## bool = Boleano
print('Python') ## Str = String

## Variáveis

age = 31
name = 'Marcos'
print(f'Meu nome é {name} e eu tenho {age} anos de idade.')

age = 30
name = 'Marcos Carrijo'
print(f'Meu nome é {name}, e eu tenho {age} anos de idade.')

## Constantes
## Uma constante é imutável, porém no Python, nada é imutável.
## Python não tem uma palavra reservada como o final do Java.
## Mas se a Variavel tiver o nome em maiusculo é considerado como constante perante a convensão de programadores.

## Boas prática
## Snake case: Preço total = preco_juros
## Escolher nomes sugestivos: Exibir saldo = exibir_saldo (manutenção mais fácil)
## Nome de constantes todo em maiúsulo.

# Variáveis
nome = 'Marcos'
idade = 30

idade = 31
print(nome, idade)

limite_saque_diario = 1000

print(f'O limite diário do {nome}, é de {limite_saque_diario}')

# Constantes
BRAZILIAN_STATES = ["SP", "RJ", "MG", "SC"]

print(f'No Brasil, os estados que já conheço são: {BRAZILIAN_STATES}')
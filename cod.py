print("Hello, world!")
nome = str(input('Digite seu nome: '))
idade = int(input('Informe sua idade: '))
print(f'seja bem vindo {nome}')
if idade >= 18:
    print(f'{nome} tem {idade} e está autorizado a dirigir.')
else:
    print(f'{nome} tem {idade} e não está autorizado a dirigir.')
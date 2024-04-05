print('-' * 13)
print("Hello, world!")
print('-' * 13)
nome = str(input('Digite seu nome: '))
idade = int(input('Informe sua idade: '))
hab = str(input('Você tem habilitação [S]/[N]? ')).upper().strip()
print(f'seja bem vindo {nome}')
if idade >= 18 and hab == 'S':
    print(f'{nome} tem {idade} e está autorizado a dirigir.')
else:
    print(f'{nome} tem {idade} e não está autorizado a dirigir.')
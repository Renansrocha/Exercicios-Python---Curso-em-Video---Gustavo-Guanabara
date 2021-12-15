'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''

valores = list()

while True:
    num = int(input('Digite um valor: '))
    if num in valores:
        print('Valor duplicado! Não será adicionado.')
    else:
        valores.append(num)
        print('Valor adicionado com sucesso!')
    resposta = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while resposta not in 'SN':
        resposta = str(input('Tente novamente. Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resposta == 'N':
        break
print('=' * 30)
valores.sort()
print(f'Você digitou os valores {valores}')





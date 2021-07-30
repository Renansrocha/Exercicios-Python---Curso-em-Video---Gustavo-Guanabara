"""Exercício Python 66
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados
e qual foi a soma entre eles (desconsiderando o flag)"""

cont = soma = 0  # As 3 variáveis tem o mesmo valor
while True:   # Loop infinito
    n = int(input("Digite um número [999 para parar] "))
    if n == 999:
        break  # break ara para o loop dentro do If se for 999, antes da soma abaixo.
    cont += 1
    soma += n
print("Você digitou {} vezes. e a soma dos valores é {}".format(cont, soma))

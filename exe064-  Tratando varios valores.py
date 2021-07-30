'''Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados
e qual foi a soma entre eles (desconsiderando o flag)'''

n = cont = soma = 0  # As 3 variavéis tem o mesmo valor
n = int(input("Digite um número [999 para parar] "))
while n != 999:
    cont += 1
    soma += n
    n = int(input("Digite um número [999 para parar] ")) # Input na ultima linha para desconsiderar o flag 999
print("Você digitou {} vezes. e a soma dos valores é {}".format(cont, soma))
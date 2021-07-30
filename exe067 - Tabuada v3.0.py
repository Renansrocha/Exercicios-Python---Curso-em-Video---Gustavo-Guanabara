"""Exercício Python 67
Faça um programa que mostre a tabuada de vários números, 
um de cada vez, para cada valor digitado pelo usuário. 
O programa será interrompido quando o número solicitado for negativo."""""
n = c = 0
while True:
    n = int(input("Você quer ver a tabuada de qual valor? "))
    print("_" * 30)
    if n < 0:
        print("Programa de tabuada finalizado. Volte sempre!")
        break
    for c in range(1, 11):
        print('{} x {:2} = {}'.format(n, c, n * c))
    print("_"*30)

"""Exercício Python 63: Escreva um programa que leia um número N
inteiro qualquer e mostre na tela os N primeiros elementos de uma
Sequência de Fibonacci. Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8"""

print("\033[1;97;41m=\033[m"*22)
print("\033[1;97mSequencia de Fibonacci")
print("\033[1;97;41m=\033[m"*22)
n = int(input("Quantos termos você quer mostrar?: "))
t1 = 0  # Primeiro termo da sequencia
t2 = 1  # Segundo termo da sequencia
print("~"*22)
print("{} -> {} ".format(t1, t2), end=" ")
contador = 3 # Começa apartir do 3 pois irá para o terceiro termo
while contador <= n:
    t3 = t1 + t2 # Em While essa sequencia se desloca, somando automaticamente os proximos termos t4, t5, t6 etc...
    print("-> {} ".format(t3), end="")
    contador += 1
    t1 = t2  # Fomula para o deslocamento dentro do While
    t2 = t3  # omula para o deslocamento dentro do While
print("-> Fim")

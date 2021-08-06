"""Exercício Python 72:
Crie um programa que tenha uma tupla totalmente preenchida
 com uma contagem por extenso, de zero até vinte.
 Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso."""

cont = "Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis",\
       "Sete", "Oito", "Nove", "Dez", "Onze", "Doze", "Treze", "Quartose", \
       "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte"
while True:
    n = int(input("Digite um número entre 0 e 20: "))
    if 0 <= n <= 20:
        break
    print("Tente novamente. ", end="")
print(f"Você digitou o número {cont[n]}")




''' while n != '0 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20':
'''


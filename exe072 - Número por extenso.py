"""Exercício Python 72:
Crie um programa que tenha uma tupla totalmente preenchida
 com uma contagem por extenso, de zero até vinte.
 Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso."""

cont = "Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", \
       "Sete", "Oito", "Nove", "Dez", "Onze", "Doze", "Treze", "Quartose", \
       "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte"
while True:
    n = int(input("Digite um número entre 0 e 20: "))
    if 0 <= n <= 20:
        print(f"Você digitou o número {cont[n]}")
        resposta = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
    if 0 > n > 20:
        print("Tente novamente. ", end=" ")
    while resposta not in "SN":
        resposta = str(input("Resposta inválida, por favor informe sim = [S] ou [N] = não:")).strip().upper()[0]
    if resposta == "N":
        break
print("Obrigado. Volte sempre!")

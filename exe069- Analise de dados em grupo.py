'''Exercício Python 69:
Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''

maiorde18 = 0  # Contador para maiores de 18 anos
homemcadastrado = 0  # Contador para homens cadastrados
totalmulhermenorde20 = 0  # Contador de mulheres menores de 20
while True:
    print("--" * 10)
    print("\033[1;33mCADASTRE UMA PESSOA\033[m")
    print("--" * 10)
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]
    while sexo not in "MF":
        sexo = str(input("Dados inválidos. Por favor, informe um sexo:")).strip().upper()[0]
    print("--" * 10)
    if sexo == "M":
        homemcadastrado += 1
    if sexo == "F" and idade < 20:
        totalmulhermenorde20 += 1
    if idade >= 18:
        maiorde18 += 1
    resposta = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
    while resposta not in "SN":
        resposta = str(input("Resposta inválida, por favor informe sim = [S] ou [N] = não:")).strip().upper()[0]
    if resposta == "N":
        break
print("Ao todo temos {} pessoas com mais de 18 anos".format(maiorde18))
print("Ao todo temos {} homens cadastrado".format(homemcadastrado))
print("Ao todo temos {} mulheres com menos de 20 anos".format(totalmulhermenorde20))

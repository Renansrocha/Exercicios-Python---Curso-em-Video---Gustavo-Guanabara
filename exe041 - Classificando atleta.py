from datetime import date
dn = int(input("Digite seu ano de nascimento: "))
idade = date.today().year - dn
print("O Atleta tem {} anos.".format(idade))
if idade <= 9:
    print("Classificação: MIRIM ")
elif idade <= 14:
    print("Classificação: INFANTIL ")
elif idade <= 19:
    print("Classificação: JÚNIOR ")
elif idade <= 25:
    print("Classificação: SÊNIOR ")
elif idade > 25:
    print("Classificação: MASTER ")


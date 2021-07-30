sexo = int(input("""Informe o seu sexo: 
[ 1 ] \033[4;33mMasculino\033[m
[ 2 ] \033[4;33mFeminino\033[m
Opção: """))
from datetime import date
if sexo == 1:
    nasc = int(input("Informe o ano do seu nascimento: "))
    hoje = date.today().year
    resta = 18 - (hoje - nasc)
    passou = (hoje - nasc) - 18
    idade = hoje - nasc

    print("Quem nasceu em {} tem {} anos em {}.".format(nasc, idade, hoje))
    if idade > 18:
        print("Você já deveria ter se alistado ha {} anos.".format(passou))
        print("Seu alistamento foi em {}".format(nasc + 18))
    elif idade < 18:
        print("Você irá se alistar daqui há {} anos.".format(resta))
        print("Seu alistamento será em {}.".format(nasc + 18))
    else:
        print("Você tem que se alistar IMEDIATAMENTE!")
elif sexo == 2:
    print("Você não precisa se alistar.")
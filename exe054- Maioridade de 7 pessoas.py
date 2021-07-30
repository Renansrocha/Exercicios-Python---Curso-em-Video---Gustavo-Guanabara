from datetime import date
atual = date.today().year  # Data atual
totalmaior = 0  # Contador para o IF
totalmenor = 0  # Contador para o ELSE
for c in range(1, 8):  # For com 7 repetições
    dn = int(input("Digite o ano de nascimento da {}º pessoa: ".format(c))) # Entrada da data de nascimento com contagem do for de 1 a 7
    idade = atual - dn  # Calculo idade
    if idade >= 18:  # Se idade menor que 18
        print("Você tem {} anos.\033[1;34m Já é \033[mmaior de idade.".format(idade))
        totalmaior += 1  # Contador
    else:  # Se não
        print("Você tem {} anos.\033[1;34m Não é \033[m é maior de idade".format(idade))
        totalmenor += 1  # Contador
print("{} pessoas são maiores de idade".format(totalmaior))
print("{} pessoas ainda são menores de idade".format(totalmenor))


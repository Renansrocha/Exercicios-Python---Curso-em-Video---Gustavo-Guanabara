maior = 0
menor = 0
for c in range(1, 6):  # For com 5 repetições
    peso = float(input("Digite o peso da  {}º pessoa: ".format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:  # Se não
        if peso > maior:
                maior = peso
        if peso < menor:
                menor = peso
print("O maior peso é {}.".format(maior))
print("O menor peso é {}".format(menor))


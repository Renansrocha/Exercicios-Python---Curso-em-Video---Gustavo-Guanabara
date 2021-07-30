somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = 0
totalmulher20 = 0
for c in range(1, 5):
    print("======={}º PESSOA =======".format(c))
    nome = str(input("Nome: ")).upper().strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo  [M]/[F]: ")).upper().strip()
    somaidade += idade
    if c == 1 and sexo in 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "M" and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "F" and idade > 20:
        totalmulher20 += 1
mediaidade = somaidade / 4
print("A média de idade do grupo é {:.0f} anos".format(mediaidade))
print("O homem mais velho tem {} anos e se chama {}".format(maioridadehomem, nomevelho))
print("Ao todo são {} mulheres com menos de 20 anos".format(totalmulher20))

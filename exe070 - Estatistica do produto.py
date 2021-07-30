'''Exercício Python 70:
 Crie um programa que leia o nome e o preço de vários produtos.
 O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''

cont = 0  # Contador inicialmente com 0 para analisar e contar os produtos que serão declarados com menor valor
maisbarato = " "  # Variavel com espaço vazio para receber o nome do produto mais barato.
totmil = 0  # Contador inicialmente com 0  que irá contar produtos acima de 1000,00
soma = 0  # Variavel inicialmente com 0 que irá somar as repetiçoes das variaves de preço
print("=" * 20)
print("\033[1;97mLOJA DO PROGRAMADOR\033[m")
print("=" * 20)
while True:
    produto = str(input("Nome do produto: ")).strip()
    preco = float(input("Preço do produto R$"))
    cont += 1
    soma += preco
    if preco >= 1000:
        totmil += 1
    if cont == 1:  # Irá analisar o primeiro produto
        menor = preco  # Variavel menor recebe o valor do primeiro produto
        barato = produto
    else:
        if preco < menor:  # Se o proximo preço for menor que o anterior declarado na variavel "Menor":
            menor = preco  # A variavel menor irá receber o valor do menor preço dentro do loop while
            barato = produto
    resposta = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
    while resposta not in "SN":
        resposta = str(input("Resposta inválida, por favor informe sim = [S] ou [N] = não:")).strip().upper()[0]
    if resposta == "N":
        break
print(f"O total de compra foi de R${soma:.2f}")
if preco >= 1000:
    print(f"Temos {totmil} produto acima de R$1000,00.")
print(f"O produto mais barato foi {barato} que custa R${menor:.2f}")
print("=" * 20)
print("\033[1;97mFIM DO PROGRAMA\033[m")
print("=" * 20)

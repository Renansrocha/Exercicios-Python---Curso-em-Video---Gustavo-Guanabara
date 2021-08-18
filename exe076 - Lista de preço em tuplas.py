print("-" * 40)
print(f'\033[1;97;41m{"LISTAGEM DE PREÇOS":^40}\033[m')  #Centralizando texto utilizando ":^40", dentro do format, com aspas duplas
print("-" * 40)
produtos = ("Lápis", 1.75,
            "Borracha", 2.00,
            "Caderno", 15.90,
            "Estojo", 25.00,
            "Transferidor", 4.20,
            "Compasso", 9.99,
            "Mochila", 120.32,
            "Canetas", 22.30,
            "Livro", 34.90)
for posição in range(0, len(produtos)):  #Usando for in range, iniciando com 0 e utilizando Len para listar
    if posição % 2 == 0:  #produtos inicia na posição0 ou seja par
        print(f"{produtos[posição]:.<30}", end="")
    else:  #preços inicia na posição 1 ou seja impar
        print(f"R${produtos[posição]:>7.2f}")
print("-" * 40)


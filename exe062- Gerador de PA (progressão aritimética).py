#Exercício Python 62: Melhore o DESAFIO 61,
# perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
termo = primeiro
contador = 1
total = 0  # contador total dos termos
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print("{} ->".format(termo), end="")
        termo += razao
        contador += 1
    print("Pausa")
    mais = int(input("Quantos termos você quer mostrar a mais? "))
print(f"Progressão finalizada \ncom {total} termos mostrados")
# \n quebra formatação para linha de baixo
# f antes das "" usando colchetes {} simplifica o .format


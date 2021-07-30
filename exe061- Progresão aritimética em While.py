primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
contador = 1
while contador <= 10:
    print("{} ->".format(primeiro), end="")
    primeiro += razao
    contador += 1
print("Acabou")

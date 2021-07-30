print("\033[4;34m=\033[m"*30)
print("     10 TERMOS DE UMA PA")
print("\033[4;34m=\033[m"*30)
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
decimo = primeiro + (10-1) *razao
for c in range(primeiro, decimo + razao, razao):
    print("{}".format(c), end=" > ")
print("Acabou")
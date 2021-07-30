n = int(input("Digite um numero para saber se ele é primo: "))
total = 0
for c in range(1, n+1):
    if n % c == 0:
        print("\033[1;32m", end=' ')
        total += 1
    else:
        print(("\033[1;30m"), end=' ')
    print("{}".format(c), end=' ')
print("\n\033[mO número {} foi divisivel {} vezes".format(n, total))
if total == 2:
    print("E por isso ele È um número primo!")
else:
    print("E por isso ele NÂO é um número primo")
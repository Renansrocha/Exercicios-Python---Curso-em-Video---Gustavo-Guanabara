'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
 No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''

listnum = []
maior = menor = 0
for c in range(0, 5):
    listnum.append(int(input(f"Digite um valor na posição {c}:")))
    if c == 0:
        maior = menor = listnum[c]
    else:
        if listnum[c] > maior:
            maior = listnum[c]
        if listnum[c] < menor:
            menor = listnum[c]
print("=-"*20)
print(f"Você digitou os valores {listnum}")
print(f"O maior valor digitado foi {maior} nas posições ", end="")
for i, v in enumerate(listnum):
    if v == maior:
        print(f"{i}...", end="")
print(f"\nO menor valor digitado foi {menor} nas posições ", end="")
for i, v in enumerate(listnum):
    if v == menor:
        print(f"{i}...", end="")

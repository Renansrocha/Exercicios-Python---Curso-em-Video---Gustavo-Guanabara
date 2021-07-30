soma: int = 0 # Acumulador
cont = 0 # Contador
for c in range(1, 501, 2):
    if c % 3 == 0:
         soma += c  # Forma simplificada que equivale a  soma = soma + c
        cont += 1  # Forma simplificada que equivale a  soma = cont = cont + 1
print(" A soma de todos os {} valores solicitado é {}.".format(cont, soma))





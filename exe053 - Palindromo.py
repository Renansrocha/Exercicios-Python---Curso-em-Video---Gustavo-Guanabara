frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split() # GERAR LISTA
juntos = ''.join(palavras) # JUNTAR LISTA PARA ELIMINAR OS ESPAÇOS
inverso = juntos[::-1] # FORMA SIMPLIFICADA USANDO FATIAMENTO
'''for letra in range(len(juntos)-1, -1, -1): # GEROU O INVERSO DE UMA STRING, DA ULTIMA LETRA ATÉ A PRIMEIRA VOLTANDO UMA LETRA
    inverso += juntos[letra] # VERIFICA SE O -INVERSO- É O MESMO QUE -JUNTO-'''
print("O inverso de {} é {}.".format(juntos, inverso))
if inverso == juntos:
    print("A frase é um PALINDRÓMO")
else:
    print("A frase NÂO é um PALINDRÓMO")

# inverter um string [::-1]
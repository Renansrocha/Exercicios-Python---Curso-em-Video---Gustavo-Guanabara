sexo = str(input("Digite seu sexo: \033[1;41;97m M \033[m (masculino)   \033[1;41;97m F \033[m (feminino): ")).strip().upper()[0]
while sexo not in "M F":
      sexo = str(input("Dados invalidos. Por favor, informe um sexo:")).strip().upper()[0]
print("Sexo {} registrado com sucesso. Muito obrigado!".format(sexo))
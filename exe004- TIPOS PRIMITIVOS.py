a = input('Digite algo: ')
print("O tipo primitivo desse valor é", type(a))
print("Só tem ""\033[4;33m""espaços""\033[m""?", a.isspace())
print("È um ""\033[4;33m""número""\033[m""?", a.isnumeric())
print("È ""\033[4;33m""alfabético""\033[m""?", a.isalpha())
print("È ""\033[4;33m""alfanúmerico""\033[m""?", a.isalnum())
print("Está em ""\033[4;33m""maisculo""\033[m""?", a.isupper())
print("Está em ""\033[4;33m""minusculo""\033[m""?", a.isalnum())
print("Está ""\033[4;33m""capitalizada""\033[m""?", a.istitle())

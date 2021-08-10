"""Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros
colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
 Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense."""

times = ("Atlético - MG", "Palmeiras", "Fortaleza", "Bragantino", "Flamengo", "Atlético PR", "Ceara SC",
         "Santos", "Atlético GO", "Bahia", "Internacional", "Corinthians", "Fluminense", "Juventude ",
         "Sport Recife", "São Paulo", "America MG", "Cuiaba", "Grêmio", "Chapecoense")
print(f"\033[1;30;43mLista de times do Brasileirão 09/08/2021:\033[m \n"
      f"\033[4;32m{times}\033[m")
print(f"\033[1;30;43mOs 5 primeiros são:\033[m \n"
      f"\033[4;34m{times[0:5]}")
print(f'\033[1;30;43mOs 4 últimos são:\033[m \n'
      f'\033[4;31m{times[-4:]}')
print(f'\033[1;30;43mTimes em ordem alfabética: \033[m \n'
      f'\033[4;97m{sorted(times)}')
print(f'\033[1;30;43mO Chapecoense está na :\033[m \n'
      f'\033[4;31m{times.index("Chapecoense")+1} posição')
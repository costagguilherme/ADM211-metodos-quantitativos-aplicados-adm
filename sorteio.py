from random import randint
import pandas as pd

sorteados = set()
while len(sorteados) < 32:
    sorteados.add(randint(0, 200))

print(len(sorteados))
print(sorteados)

arquivo = 'olimpiadas.xlsx'
planilha = pd.read_excel(arquivo)

paises_sorteados = []
for indice, linha in planilha.iterrows():
    if indice in sorteados:
        paises_sorteados.append({
            'linha': indice + 2,
            'pais': linha['pais']
        })

with pd.ExcelWriter(arquivo, engine='openpyxl', mode='a') as writer:
    pd.DataFrame(paises_sorteados).to_excel(writer, sheet_name='amostra', index=False)

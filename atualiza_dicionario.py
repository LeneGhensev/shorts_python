# Atualização de dados em um dicionário

#Para não impactar as duas listas, cria-se uma cópia do dicionário
precos = {
    "iphone": 6000,
    "ipad": 10000,
    "airpod": 2500 
}

novos_precos = precos.copy()

novos_precos["airpod"] = 3000

print(precos)
print(novos_precos)
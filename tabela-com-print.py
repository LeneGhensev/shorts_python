# Criar uma tabela com print em python

tabela = {
    'id001': {'nome': 'Lene G', 'idade': 40, 'profissão': 'analista'},
    'id002': {'nome': 'Lene teste', 'idade': 50, 'profissão': 'analista 2'}
}

# Print sem a formatação

for registro in tabela.values():
    print(registro['nome'])
    
# Criação de uma tabela com indicadores de formatação, por exemplo o ^ indica que deve ser centralizado e o número posteriormente é a quantidade de espaços.

print(f"{'Nome': ^10}) | {'Idade': ^6} | {'Profissão': ^12}")
print(f"{'-'*10} | {'-'*6} | {'-'*12}")

for registro in tabela.values():
    print(f"{registro['nome']:<10} | {registro['idade']:^6} | {registro['profissão']:^12}")
# Imprimir o índice com cada item de uma lista

lista = [
    "item 1",
    "item 2",
    "item 3",
    "item 4"
]
    
#para imprimir o índice com cada item, porém com uma "cara de iniciante"
i = 0
for item in lista:
    print(i, item)
    i += 1
    
#para imprimir o índice com cada item, porém usando o enumerate que pega os índices e atribui numa variável
for i, item in enumerate(lista):
    print(i,item)

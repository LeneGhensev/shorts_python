#Criação de condição para uma lista

vendas = range(1000, 5000)

print(list(vendas))

def bateu_meta(venda):
    if venda > 4000:
        return True
    else: 
        return False
    
bateram_meta = filter(bateu_meta, vendas) #filter é uma função padrão do python para filtrar informações desejadas. Passa pra ela a função criada e a lista que se quer filtrar.

print('\nBateram a meta', list(bateram_meta))
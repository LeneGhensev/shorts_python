#Fazer um cálculo sobre cada um dos itens da lista do dicionário e criar um novo dicionário

vendas = {
    "iphone": 2000,
    "motorola": 3000,
    "samsung": 5000
}

#list comprehension
imposto = [vendas[item]*0.1 for item in vendas]
print(imposto)

#dictionary comprehension
imposto2 = {item: vendas[item]*0.1 for item in vendas}
print(imposto2)
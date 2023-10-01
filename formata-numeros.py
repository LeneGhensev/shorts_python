# Formatação de números

numeros = {5.3, 65.823, -23.16, 6, 0.2, 0.33333}

for numero in numeros:
    print (numero)
    

print ('Com 2 casas decimais')
for numero in numeros:
    print (f'{numero:.2f}')
    
print ('Para alinhar as casas decimais')
for numero in numeros:
    print (f'{numero:10.2f}')
    
print ('Para retirar os zeros')
for numero in numeros:
    print (f'{numero:10.2f}'.rstrip('0').rstrip('.'))
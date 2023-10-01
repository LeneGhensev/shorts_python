# Printar com cores

from colorama import init, Fore, Back

init()

print(Fore.GREEN + "Imprime texto na cor verde")
print(Back.RED + "Imprime texto com background vermelho")
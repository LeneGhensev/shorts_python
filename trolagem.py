import pyautogui as py
import random
import time

time.sleep(5)

mensagens= ["Oi, tudo bem?", "E aí", "Como vai?", "Aqui tá tudo bem"]

for i in range(5):
    msg = random.choice(mensagens)
    py.write(msg)
    py.press("enter")
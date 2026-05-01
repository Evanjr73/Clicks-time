import pyautogui
import time

# Tempo em segundos (10 minutos = 600 segundos)
intervalo = 100

print("O script começará em 5 segundos...")
time.sleep(5)

while True:
    pos = pyautogui.position()
    print(f"Posição atual do mouse: {pos}")
    pyautogui.click()  # Clica na posição atual do mouse
    print("Clique realizado!")
    time.sleep(intervalo)  # Espera pelo intervalo definido antes de clicar novamente
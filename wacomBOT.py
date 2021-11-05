from pynput.mouse import Button, Controller
import time
import os

os.startfile('C:\Program Files\Tablet\Pen\Consumer_CPL.exe')

mouse = Controller()
time.sleep(0.5)
mouse.position = (787, 328) ## CLIQUE NA ABA CANETA
mouse.click(Button.left, 1)
time.sleep(0.25)
mouse.position = (1134, 418) ## CLIQUE NO MAPEAMENTO DA CANETA
mouse.click(Button.left, 1)
time.sleep(0.25)
mouse.position = (717, 627) ## CLIQUE PARA DEFINIR QUE VAI SER UMA PARTE DA AREA
mouse.click(Button.left, 1)
time.sleep(0.25)
mouse.position = (905, 626) ## CLIQUE PARA ABRIR O MENU DA DEFINIÇÂO DA AREA
mouse.click(Button.left, 1)
time.sleep(0.25)

i = 917
j = 461

while (j > 452):
    time.sleep(.001)
    mouse.position = (905, j)
    j -= 1

while (i < 928):
    time.sleep(.001)
    mouse.position = (i, 452)
    i+=1

mouse.position = (928, 452) ## PRIMEIRO CLIQUE DO DRAG
mouse.press(Button.left)
time.sleep(0.25)

i = 928
j = 452

while (j < 490):
    time.sleep(.001)
    mouse.position = (i, j)
    j += 1
while (i < 980):
    time.sleep(.001)
    mouse.position = (i, j)
    i+=1

mouse.position = (980, 490) ## ARRASTADA
mouse.release(Button.left)
time.sleep(1)

mouse.position = (989, 497) ## MOVIMENTO PARA MOVIMENTAR A AREA
mouse.press(Button.left)
time.sleep(1)

i = 989
j = 497

while (j > 489):
    time.sleep(.001)
    mouse.position = (i, j)
    j -= 1

while (i > 980):
    time.sleep(.001)
    mouse.position = (i, j)
    i-=1

mouse.position = (980, 489) ## MOVIMENTO PARA MOVIMENTAR A AREA
mouse.release(Button.left)
time.sleep(0.05)
mouse.position = (1087, 738) ## ok
mouse.click(Button.left, 1)
time.sleep(0.05)
mouse.position = (1155, 701) ## ok
mouse.click(Button.left, 1)
time.sleep(0.05)
mouse.position = (1233, 300) ## fecha
mouse.click(Button.left, 1)

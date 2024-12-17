import pyautogui
import pydirectinput
import time
import keyboard
import cv2
import numpy as np
import os
import random


#definitions
yellow1 = (231, 180, 119)
loop = 0
ncount = 0




def funcion_para_numero(n):
    if n == 1:
        click_cuadricula_divine_cards(1295, 615, 52, 47)
    elif n == 2:
        click_cuadricula_eight_slots_quad(40, 185, 52, 108)
    elif n == 3:
        click_cuadricula_four_slots_quad(40, 148, 52, 52)
    elif n == 4:
        click_cuadricula_six_slots_quad(42, 165, 53, 78)
    elif n == 5:
        click_cuadricula_three_slots_quad(25, 165, 28, 78)
    else:
        print(f"Número {n} ingresado. No hay acciones definidas para este número.")


def comprobar_color_con_opencv(region_x, region_y, region_ancho, region_alto,tolerancia=20):
    # region of the screen
    screenshot = pyautogui.screenshot(region=(region_x, region_y, region_ancho, region_alto))
    img = np.array(screenshot)

    nombre_archivo = "captura.png"

    # path 
    carpeta_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_completa = os.path.join(carpeta_actual, nombre_archivo)
    screenshot.save(ruta_completa)

    # Convert RGB to BGR OpenCV
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    # Convert BGR to HSV
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # range HSV
    color_objetivo_hsv = cv2.cvtColor(np.uint8([[yellow1]]), cv2.COLOR_RGB2HSV)[0][0]

    # checkpoint to ensure color
    lower_hue = max(int(color_objetivo_hsv[0]) - tolerancia, 0)
    upper_hue = min(int(color_objetivo_hsv[0]) + tolerancia, 179)

    lower_bound = np.array([lower_hue, 50, 50])  # test 50
    upper_bound = np.array([upper_hue, 255, 255])

    # mask of colors
    mask = cv2.inRange(hsv_img, lower_bound, upper_bound)

    # test mode to see what it displays
    #cv2.imshow('Mascara', mask)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    # check if there is pixels
    if cv2.countNonZero(mask) > 0:
        return True
    else:
        return False
  
############################################################################################################
############################################################################################################

def click_cuadricula_three_slots_quad(inicio_x, inicio_y, incremento_x, incremento_y, columnas=7, filas=8): # 12

    global loop
    if loop == 0:
        pydirectinput.keyDown('shift')

    # reset variables `x` and `y` to initial values
    x = inicio_x
    y = inicio_y
    
    if loop == 0:
        pydirectinput.rightClick(1295, 615)

    time.sleep(0.05)

    for fila in range(filas):
        for columna in range(columnas):
            # first click
            pydirectinput.moveTo(x, y)

            time.sleep(0.005)

            region_ancho, region_alto = 15, 40  # adjust size of the box
            captura_x = round(x - (region_ancho / 2))  # round x
            captura_y = round(y - (region_alto / 2.35))   # round y
            region_ancho = round(region_ancho)
            region_alto = round(region_alto)

            if comprobar_color_con_opencv(captura_x, captura_y, region_ancho, region_alto):
                pass
            else:
                pydirectinput.click(x, y)

            # salt to next box
            x += incremento_x

            # stop key
            if keyboard.is_pressed('F7'):
                pydirectinput.keyUp('shift')
                return

        
        x = inicio_x  # reset x to initial value of the row
        y += incremento_y  # set up y to the next row

    # at the end of the cycle, increase the loop to continue with the next refill if necessary
    loop += 1

    # this is not good, refactor it
    click_cuadricula_three_slots_quad(inicio_x, inicio_y, incremento_x, incremento_y)

############################################################################################################
############################################################################################################

def click_cuadricula_four_slots_quad(inicio_x, inicio_y, incremento_x, incremento_y, columnas=7, filas=12): # 12

    global loop,ncount
    if loop == 0:
        pydirectinput.keyDown('shift')


    x = inicio_x
    y = inicio_y
    
    if loop == 0:
        pydirectinput.rightClick(1295, 615)

    time.sleep(0.01)

    for fila in range(filas):
        for columna in range(columnas):

            pydirectinput.moveTo(x, y)


            region_ancho, region_alto = 40, 40  
            captura_x = round(x - (region_ancho / 2.35))  
            captura_y = round(y - (region_alto / 2.9))   
            region_ancho = round(region_ancho)
            region_alto = round(region_alto)

            if comprobar_color_con_opencv(captura_x, captura_y, region_ancho, region_alto):
                pass
            else:
                pydirectinput.click(x, y)
                ncount = ncount + 1
                print(f"Alterations usados {ncount}")
            

            x += incremento_x

            if keyboard.is_pressed('F7'):
                pydirectinput.keyUp('shift')
                return

        x = inicio_x 
        y += incremento_y 

    loop += 1

    click_cuadricula_four_slots_quad(inicio_x, inicio_y, incremento_x, incremento_y)
        
############################################################################################################
############################################################################################################

def click_cuadricula_eight_slots_quad(inicio_x, inicio_y, incremento_x, incremento_y, columnas=7, filas=6):
    global loop,ncount
    if loop == 0:
        pydirectinput.keyDown('shift')

    x = inicio_x
    y = inicio_y
    
    if loop == 0:
        pydirectinput.rightClick(1295, 615)

    time.sleep(0.01)

    if ncount > 15000:
        return
    
    for fila in range(filas):
        for columna in range(columnas):
            pydirectinput.moveTo(x, y)



            region_ancho, region_alto = 40, 80
            captura_x = round(x - (region_ancho / 2.35))
            captura_y = round(y - (region_alto / 1.85))
            region_ancho = round(region_ancho)
            region_alto = round(region_alto)

            if comprobar_color_con_opencv(captura_x, captura_y, region_ancho, region_alto):
                pass
            else:
                pydirectinput.click(x, y)
                ncount = ncount + 1
                print(f"Alterations usados {ncount}")
            
            x += incremento_x

            if keyboard.is_pressed('F7'):
                pydirectinput.keyUp('shift')
                return

        x = inicio_x 
        y += incremento_y 


    loop += 1

    click_cuadricula_eight_slots_quad(inicio_x, inicio_y, incremento_x, incremento_y)

############################################################################################################
############################################################################################################

def click_cuadricula_six_slots_quad(inicio_x, inicio_y, incremento_x, incremento_y, columnas=1, filas=3):
    global loop
    if loop == 0:
        pydirectinput.keyDown('shift')

    x = inicio_x
    y = inicio_y
    
    if loop == 0:
        pydirectinput.rightClick(1295, 615)

    time.sleep(0.05)

    for fila in range(columnas):
        for columna in range(filas):
            pydirectinput.moveTo(x, y)

            tiempo = random.uniform(0.005,0.01)
            time.sleep(tiempo)

        
            region_ancho, region_alto = 40, 50 
            captura_x = round(x - (region_ancho / 2.35))  
            captura_y = round(y - (region_alto / 2.35))   
            region_ancho = round(region_ancho)
            region_alto = round(region_alto)

            if comprobar_color_con_opencv(captura_x, captura_y, region_ancho, region_alto):
                pass
            else:
                pydirectinput.click(x, y)
            
            x += incremento_x

            if keyboard.is_pressed('F7'):
                pydirectinput.keyUp('shift')
                return

        x = inicio_x
        y += incremento_y  

    loop += 1

    click_cuadricula_six_slots_quad(inicio_x, inicio_y, incremento_x, incremento_y)

############################################################################################################
############################################################################################################

def click_cuadricula_divine_cards(inicio_x, inicio_y, incremento_x, incremento_y, columnas=12, filas=5):
    pydirectinput.keyDown('ctrl')

    try:
        x = inicio_x
        y = inicio_y

        for fila in range(filas):
            for columna in range(columnas):

                pydirectinput.click(x, y)
                time.sleep(0.1)  
                pydirectinput.click(631, 730) 
                time.sleep(0.1) 
                pydirectinput.click(627, 446)
                time.sleep(0.1) 
                x += incremento_x

                # Comprobar si se ha presionado la tecla de parada
                if keyboard.is_pressed('F7'):
                    pydirectinput.keyUp('shift')
                    return
                
            x = inicio_x
            y += incremento_y
    finally:
        pydirectinput.keyUp('ctrl')


# Programa principal

def main():
    pyautogui.FAILSAFE = True
    pydirectinput.FAILSAFE = False


    funcion_para_numero(2) #hardcoded
if __name__ == "__main__":
    main()
